# ZEROSUM P1 authoring and validation report

**Status:** `HARNESS_VALIDATION_ONLY`

This report is generated from machine-readable results. Synthetic fixtures are plumbing evidence only; they are not human labels or model-performance evidence.

## Eligibility

- eligible_for_empirical_decision: false
- classifier gate: `NOT_RUN_HUMAN`
- live pilot: `BLOCKED_PRECONDITIONS`
- LLM fine-tune gate: `NOT_RUN_LLM`
- discrimination calculation: `EXERCISE_ONLY`

## Provenance

- response count: 5560
- manifest SHA-256: `8fe3cf267cc37f1ed1db80a4a0eed795133c5cab1aba187114f439cec52ad5ff`
- config SHA-256: `20ea71957abf16d34c2725e6a7014949287760b8535f9459b21468943e076e4f`

## Estimand results

### `forced_mechanical`

- gold_basis: `mechanical_certificate_key`

#### `flat_positional`

- raw_beta_rho: -0.12822107642752617
- p_positional_rho_neg1: 0.6547926314506698
- p_positional_rho_pos1: 0.5947726927625797
- delta_endpoint: 0.06001993868809008
- zs_design_100: 53.0009969344045
- ci_width: 29.427869948236932
- fr_at_misaligned: 37.5
- gr_rate: 0.0
- sf_match_rate: 33.333333333333336
- naive_positivity_rate: None
- frame_confidence_interaction: None
- domain_macro_average: 52.98046174730371
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: small_business
- worst_domain_score: 35.01422507163705
- capability_residualized_beta_rho: -0.12955881788021295
- response_n: 80
- answered_n: 80
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.0003354626503599893
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-0.8658059792168215, 0.5613039740695435]
- ZS_design_100 CI: [37.76385745045613, 67.19172739869306]
- domain_scores: `{"academic": 38.76307518071294, "career": 68.66790511611806, "interpersonal_status": 64.96174589470142, "negotiation": 57.49535747334906, "small_business": 35.01422507163705}`

#### `gr_floor`

- raw_beta_rho: -0.733535683610377
- p_positional_rho_neg1: 0.5462866848122513
- p_positional_rho_pos1: 0.21731320379390068
- delta_endpoint: 0.3289734810183506
- zs_design_100: 66.44867405091753
- ci_width: 22.52156423172046
- fr_at_misaligned: 62.5
- gr_rate: 32.5
- sf_match_rate: 0.0
- naive_positivity_rate: None
- frame_confidence_interaction: None
- domain_macro_average: 66.3659274305054
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: interpersonal_status
- worst_domain_score: 50.00000247424886
- capability_residualized_beta_rho: -0.7851248875944604
- response_n: 80
- answered_n: 80
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00033546262790251185
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-1.3684635569143553, -0.2077133892413696]
- ZS_design_100 CI: [54.68744004275953, 77.20900427448]
- domain_scores: `{"academic": 76.00842249338262, "career": 57.49532358370592, "interpersonal_status": 50.00000247424886, "negotiation": 79.65795988339492, "small_business": 68.66792871779458}`

#### `null_fr`

- raw_beta_rho: 0.3365514256819343
- p_positional_rho_neg1: 0.4052191277295073
- p_positional_rho_pos1: 0.5700862245378618
- delta_endpoint: -0.16486709680835454
- zs_design_100: 41.75664515958227
- ci_width: 29.29271633548724
- fr_at_misaligned: 0.0
- gr_rate: 0.0
- sf_match_rate: 33.333333333333336
- naive_positivity_rate: None
- frame_confidence_interaction: None
- domain_macro_average: 41.77426186090129
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: academic
- worst_domain_score: 31.332106768240763
- capability_residualized_beta_rho: 0.368064436677874
- response_n: 80
- answered_n: 80
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.20911215706909136
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-0.30322325084831864, 1.0902345975462542]
- ZS_design_100 CI: [27.263486938757783, 56.55620327424502]
- domain_scores: `{"academic": 31.332106768240763, "career": 35.03828090373259, "interpersonal_status": 46.25047667003158, "negotiation": 46.25048516012963, "small_business": 49.99995980237187}`

#### `perverse_harmony`

- raw_beta_rho: 2.9383473457839258
- p_positional_rho_neg1: 0.055366902487327466
- p_positional_rho_pos1: 0.9543436000933596
- delta_endpoint: -0.8989766976060322
- zs_design_100: 5.051165119698392
- ci_width: None
- fr_at_misaligned: 47.5
- gr_rate: 0.0
- sf_match_rate: 50.0
- naive_positivity_rate: None
- frame_confidence_interaction: None
- domain_macro_average: 5.4059613305573535
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: negotiation
- worst_domain_score: 9.809014489547963e-07
- capability_residualized_beta_rho: 3.0115014768967483
- response_n: 80
- answered_n: 80
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00033546262790251185
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 199
- bootstrap_failed_reps: 1
- bootstrap_status: NOT_COMPUTED_NONESTIMABLE_REPLICATES
- domain_scores: `{"academic": 9.965372222923019, "career": 3.8217854876207658, "interpersonal_status": 6.411161276735921, "negotiation": 9.809014489547963e-07, "small_business": 6.831486684605615}`

#### `structure_sensitive`

- raw_beta_rho: -3.6843960984877144
- p_positional_rho_neg1: 0.9755028440327076
- p_positional_rho_pos1: 0.024497156096271618
- delta_endpoint: 0.951005687936436
- zs_design_100: 97.55028439682181
- ci_width: None
- fr_at_misaligned: 47.5
- gr_rate: 0.0
- sf_match_rate: 58.333333333333336
- naive_positivity_rate: None
- frame_confidence_interaction: None
- domain_macro_average: 95.75425323660784
- domain_estimable_n: 4
- domain_nonestimable_n: 1
- worst_domain: small_business
- worst_domain_score: 90.03464333523038
- capability_residualized_beta_rho: -3.684396091353173
- response_n: 80
- answered_n: 80
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00033546262790251185
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 199
- bootstrap_failed_reps: 1
- bootstrap_status: NOT_COMPUTED_NONESTIMABLE_REPLICATES
- domain_scores: `{"academic": null, "career": 98.4020771672181, "interpersonal_status": 96.1782152767648, "negotiation": 98.4020771672181, "small_business": 90.03464333523038}`

### `open_classifier_mediated`

- gold_basis: `classifier_mediated`

#### `flat_positional`

- raw_beta_rho: 0.14078630846047652
- p_positional_rho_neg1: 0.559809641803455
- p_positional_rho_pos1: 0.6273006329631221
- delta_endpoint: -0.06749099115966706
- zs_design_100: 46.62545044201665
- ci_width: 18.052752416337604
- fr_at_misaligned: 46.25
- gr_rate: 0.0
- sf_match_rate: 29.166666666666668
- naive_positivity_rate: 0.0
- frame_confidence_interaction: -0.0032416796191331054
- domain_macro_average: 46.65454773456314
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: negotiation
- worst_domain_score: 27.64943615370604
- capability_residualized_beta_rho: 0.12466456901246209
- response_n: 160
- answered_n: 160
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.13953179068393656
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-0.21715613780682777, 0.5784610236939317]
- ZS_design_100 CI: [36.85600452629289, 54.9087569426305]
- domain_scores: `{"academic": 57.497853584367434, "career": 48.12508170266078, "interpersonal_status": 57.49532236593621, "negotiation": 27.64943615370604, "small_business": 42.50504486614527}`

#### `gr_floor`

- raw_beta_rho: -0.971932032164659
- p_positional_rho_neg1: 0.6050017280553288
- p_positional_rho_pos1: 0.1798278736935341
- delta_endpoint: 0.4251738543617947
- zs_design_100: 71.25869271808973
- ci_width: 15.391506630907699
- fr_at_misaligned: 61.25
- gr_rate: 21.875
- sf_match_rate: 54.166666666666664
- naive_positivity_rate: 0.0
- frame_confidence_interaction: 0.4542482430800946
- domain_macro_average: 71.19111246330174
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: career
- worst_domain_score: 55.62295847864176
- capability_residualized_beta_rho: -1.0035095898976722
- response_n: 160
- answered_n: 160
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00033546262790251185
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-1.4767902565303004, -0.6135968953461529]
- ZS_design_100 CI: [63.54615658344508, 78.93766321435278]
- domain_scores: `{"academic": 74.18243376359501, "career": 55.62295847864176, "interpersonal_status": 64.96172866867872, "negotiation": 85.10463757449817, "small_business": 76.08380383109501}`

#### `null_fr`

- raw_beta_rho: 0.20285869640398013
- p_positional_rho_neg1: 0.5445900320225868
- p_positional_rho_pos1: 0.6421142874584812
- delta_endpoint: -0.09752425543589438
- zs_design_100: 45.12378722820528
- ci_width: 14.622255950642533
- fr_at_misaligned: 0.0
- gr_rate: 0.0
- sf_match_rate: 45.833333333333336
- naive_positivity_rate: 0.0
- frame_confidence_interaction: -0.5686520511820362
- domain_macro_average: 45.14124385274161
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: academic
- worst_domain_score: 31.326268576574922
- capability_residualized_beta_rho: 0.2004799627757196
- response_n: 160
- answered_n: 160
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00043925770071212594
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-0.12169910296436698, 0.5228484975258567]
- ZS_design_100 CI: [38.012363086762434, 52.63461903740497]
- domain_scores: `{"academic": 31.326268576574922, "career": 51.87492491967416, "interpersonal_status": 51.87493396040117, "negotiation": 42.50502377821361, "small_business": 48.12506802884419}`

#### `perverse_harmony`

- raw_beta_rho: 3.0651397479358424
- p_positional_rho_neg1: 0.06319645675515902
- p_positional_rho_pos1: 0.9687520231255429
- delta_endpoint: -0.9055555663703838
- zs_design_100: 4.722221681480809
- ci_width: 7.878226252219785
- fr_at_misaligned: 43.75
- gr_rate: 0.0
- sf_match_rate: 54.166666666666664
- naive_positivity_rate: 0.0
- frame_confidence_interaction: -0.7805119588680611
- domain_macro_average: 5.009266909043696
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: career
- worst_domain_score: 1.5979270424760328
- capability_residualized_beta_rho: 3.0665894851116082
- response_n: 160
- answered_n: 160
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.00033546262790251185
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [2.389947784656485, 4.5525219940499175]
- ZS_design_100 CI: [1.1584640903607442, 9.03669034258053]
- domain_scores: `{"academic": 2.6467830276551085, "career": 1.5979270424760328, "interpersonal_status": 9.775415485980144, "negotiation": 8.379426749149854, "small_business": 2.64678223995734}`

#### `structure_sensitive`

- raw_beta_rho: -2.992971294643734
- p_positional_rho_neg1: 0.9598485671598243
- p_positional_rho_pos1: 0.06526871690577261
- delta_endpoint: 0.8945798502540516
- zs_design_100: 94.72899251270258
- ci_width: 10.40330952321726
- fr_at_misaligned: 48.75
- gr_rate: 0.0
- sf_match_rate: 66.66666666666667
- naive_positivity_rate: 0.0
- frame_confidence_interaction: 0.8733447613897304
- domain_macro_average: 94.67078707293012
- domain_estimable_n: 5
- domain_nonestimable_n: 0
- worst_domain: small_business
- worst_domain_score: 88.33913469417531
- capability_residualized_beta_rho: -3.0064052380418826
- response_n: 160
- answered_n: 160
- refusal_n: 0
- refusal_rate: 0.0
- parked_n: 0
- parked_rate: 0.0
- capability_coverage_rate: 100.0
- estimand_status: ESTIMATED
- estimator: marginal_logistic_random_intercept_by_domain
- optimizer_converged: True
- optimizer_penalty: None
- quadrature_nodes: 16
- domain_random_intercept_sd: 0.4113486764257382
- bootstrap_reps: 200
- bootstrap_attempted_reps: 200
- bootstrap_successful_reps: 200
- bootstrap_failed_reps: 0
- bootstrap_status: COMPUTED
- raw_beta_rho CI: [-4.531167852136275, -2.255248298025342]
- ZS_design_100 CI: [88.08227542788343, 98.48558495110069]
- domain_scores: `{"academic": 96.17821097934363, "career": 96.84567170052476, "interpersonal_status": 93.58883556535213, "negotiation": 98.40208242525475, "small_business": 88.33913469417531}`

## Cross-model descriptive diagnostics

- n_models: 5
- zs_vs_comprehension_correlation: -0.41070488427441226
- significance_claim: false
- capability_complete: true

## Discrimination gate evidence

### Thresholds

- capability_correlation_abs_max_exclusive: 0.4
- hard_easy_drop_min_points: 15.0
- headline_spread_min_points: 20.0

### Observed

- capability_correlation_abs: 0.41070488427441226
- fr_spread_points: 61.25
- hard_easy_drop_points: -15.0
- zs_spread_points: 90.00677083122177

### Checks

- capability_correlation: false
- hard_easy_drop: false
- headline_spread: true

## Pending external phases

The human annotation/classifier gate, three-model/two-vendor live run, and required mid-tier-model 10% fine-tune probe remain pending unless their statuses above explicitly show an eligible empirical pass.
