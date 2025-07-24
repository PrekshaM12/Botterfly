# Rollback Strategy for Model Regressions

* Deploy new model behind **feature flag**.  
* Shadow-mode 10 % traffic, compare metrics.  
* If error rate > x, flip flag to previous model (env var switch).  
* Keep both embeddings; re-index only if switch sticks.
