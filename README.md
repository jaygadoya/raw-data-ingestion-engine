# Metadata-Driven Data Pipeline

One framework, many datasets. Onboarding a new dataset means adding a row of metadata, not writing a new pipeline.

<p align="center">
  <img src="docs/pipeline.svg" alt="Animated diagram of a metadata-driven data pipeline: a metadata store feeds configuration to the Sources, Ingest, Validate, Transform and Serve stages" width="100%">
</p>

## Why metadata-driven?

- **No code per dataset.** Sources, rules, mappings and targets live in metadata tables. The pipeline code is generic.
- **Faster onboarding.** A new feed goes live by inserting a row and running the pipeline.
- **Consistent by design.** Every dataset goes through the same ingest, validate, transform and serve steps.
- **Easy to audit.** Metadata is the single source of truth for what runs, when, and how.

## How it works

1. **Register.** A dataset is described in the metadata store (connection, schema, rules, mappings, target, schedule).
2. **Read.** The orchestrator reads the metadata for each dataset that is due to run.
3. **Execute.** Generic stages (ingest, validate, transform, serve) take their instructions from that metadata.
4. **Record.** Run status, row counts and errors are written back to the metadata store.

## Metadata store

| Table / file    | Controls                                              |
| --------------- | ----------------------------------------------------- |
| `connections`   | Where to connect (host, auth method, secret name)     |
| `source_config` | What to pull (object, format, load type, watermark)   |
| `dq_rules`      | Quality checks (not null, unique, ranges, thresholds) |
| `mappings`      | Column mappings and transformation logic              |
| `target_config` | Where to publish (schema, table, write mode)          |
| `schedule`      | When to run and in what order                         |

## Example: one dataset, one config

```yaml
dataset: customer_orders
source:
  connection: sales_db
  object: public.orders
  load_type: incremental
  watermark_column: updated_at
quality:
  - rule: not_null
    columns: [order_id, customer_id]
  - rule: unique
    columns: [order_id]
transform:
  mappings:
    - { from: order_id,   to: order_key }
    - { from: order_ts,   to: order_timestamp, cast: timestamp }
target:
  schema: gold
  table: fact_orders
  write_mode: merge
schedule: "0 2 * * *"
```

## Onboard a new dataset

1. Add the connection details to `connections` (if the source is new).
2. Add a row to `source_config`, `dq_rules`, `mappings` and `target_config` for the dataset.
3. Run the pipeline. It picks up the new dataset automatically.

No code change and no redeploy.

## Repository layout

```text
.
├── docs/
│   └── pipeline.svg        # animated diagram used in this README
├── metadata/               # dataset configs / seed scripts for metadata tables
├── src/
│   ├── ingest/             # generic ingestion logic
│   ├── validate/           # rule engine driven by dq_rules
│   ├── transform/          # mapping engine driven by mappings
│   ├── serve/              # writes to targets from target_config
│   └── orchestrator/       # reads metadata and runs the stages
└── README.md
```

## Tech stack

<!-- Replace with your own stack -->

| Layer         | Technology |
| ------------- | ---------- |
| Orchestration | _your tool_ |
| Compute       | _your tool_ |
| Storage       | _your tool_ |
| Metadata      | _your tool_ |

## Contributing

Changes to pipeline behaviour should usually be a metadata change. If you need to touch the code, the change should help every dataset, not just one.
