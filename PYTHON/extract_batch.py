#!/usr/bin/env python3
"""
Batch PDF extraction worker.

Processes a single batch of PDFs assigned by generate_batch_assignments.py.
Designed to run in parallel with other batch workers.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Import extraction function from main script
from extract_ai_labs_pdfs import extract_pdf

BATCH_DIR = Path(__file__).parent.parent / "logs" / "batches"


def load_batch(batch_id):
    """Load batch assignment from JSON file."""
    batch_file = BATCH_DIR / f"batch_{batch_id}.json"

    if not batch_file.exists():
        raise FileNotFoundError(f"Batch file not found: {batch_file}")

    with open(batch_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_status(batch_id, status):
    """Save batch processing status to JSON file."""
    status_file = BATCH_DIR / f"batch_{batch_id}_status.json"
    with open(status_file, 'w', encoding='utf-8') as f:
        json.dump(status, f, indent=2)


def process_batch(batch_id, verbose=True):
    """Process all PDFs in a batch."""
    if verbose:
        print(f"=" * 60)
        print(f"Batch {batch_id} - PDF Extraction Worker")
        print(f"=" * 60)

    # Load batch assignments
    batch = load_batch(batch_id)

    if verbose:
        print(f"\nLoaded {len(batch)} PDFs to process")

    # Track results
    status = {
        'batch_id': batch_id,
        'started_at': datetime.now().isoformat(),
        'total_pdfs': len(batch),
        'processed': 0,
        'succeeded': 0,
        'failed': 0,
        'results': []
    }

    # Process each PDF
    for i, pdf_info in enumerate(batch, 1):
        pdf_path = Path(pdf_info['pdf_path'])
        output_path = Path(pdf_info['output_path'])

        if verbose:
            print(f"\n[{i}/{len(batch)}] Processing: {pdf_path.name}")

        result = {
            'pdf_filename': pdf_info['pdf_filename'],
            'pdf_path': str(pdf_path),
            'output_path': str(output_path),
            'company': pdf_info['company']
        }

        try:
            success = extract_pdf(pdf_path, output_path, verbose=verbose)

            if success:
                status['succeeded'] += 1
                result['status'] = 'success'
            else:
                status['failed'] += 1
                result['status'] = 'failed'
                result['error'] = 'extraction returned False'

        except Exception as e:
            status['failed'] += 1
            result['status'] = 'error'
            result['error'] = str(e)
            if verbose:
                print(f"✗ Error: {e}")

        status['processed'] += 1
        status['results'].append(result)

        # Save intermediate status
        save_status(batch_id, status)

    # Finalize status
    status['completed_at'] = datetime.now().isoformat()
    save_status(batch_id, status)

    # Summary
    if verbose:
        print("\n" + "=" * 60)
        print(f"Batch {batch_id} - COMPLETE")
        print("=" * 60)
        print(f"Total: {status['total_pdfs']}")
        print(f"Succeeded: {status['succeeded']}")
        print(f"Failed: {status['failed']}")
        print(f"Status saved to: {BATCH_DIR}/batch_{batch_id}_status.json")

    return status


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: extract_batch.py <batch_id>")
        print("Example: extract_batch.py 0")
        sys.exit(1)

    try:
        batch_id = int(sys.argv[1])
    except ValueError:
        print(f"Error: batch_id must be an integer, got: {sys.argv[1]}")
        sys.exit(1)

    # Check for verbose flag
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    try:
        status = process_batch(batch_id, verbose=True)

        # Exit with error code if any failures
        if status['failed'] > 0:
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
