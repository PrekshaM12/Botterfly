# Estimating Monthly Token Usage

Formula:  
`users_per_day × messages_per_user × avg_tokens × 30`

For 5 k msgs/day, 200-token average:  
`5 000 × 200 × 30 = 30 M tokens` → cost ≈ $360/mo (GPT-3.5).

Add 20 % buffer for spikes.
