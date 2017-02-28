{{cookiecutter.project_name}}
=============================

{{cookiecutter.project_short_description}}

## Running Workflow

### Environment Variables

Before running the workflow on DataFlow you must set the correct `PROJECT` and `BUCKET` environment variables to be used to execute the pipeline.

For example:

    PROJECT=your-project-id
    BUCKET=your-bucket-name

### Locally

    python {{cookiecutter.project_underscore_slug}}_main.py \
      --job_name {{cookiecutter.project_underscore_slug}}-$PROJECT \
      --project $PROJECT \
      --runner DirectRunner \
      --output ./tmp/{{cookiecutter.project_underscore_slug}}

### Google Cloud DataFlow

    python {{cookiecutter.project_underscore_slug}}_main.py \
      --job_name {{cookiecutter.project_underscore_slug}}-$PROJECT \
      --project $PROJECT \
      --runner DataflowRunner \
      --setup_file ./setup.py \
      --staging_location gs://$BUCKET/{{cookiecutter.project_underscore_slug}}/staging \
      --temp_location gs://$BUCKET/{{cookiecutter.project_underscore_slug}}/temp \
      --output gs://$BUCKET/{{cookiecutter.project_underscore_slug}}/{{cookiecutter.project_underscore_slug}}
