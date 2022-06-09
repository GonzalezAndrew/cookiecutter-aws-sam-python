# Cookiecutter SAM for Scheduled Event Python Lambda Functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Python Docker Image Serverless App using [Serverless Application Model (SAM)](https://github.com/aws/serverless-application-model).

It is important to note that you should not try to `git clone` this project but use `SAM` CLI instead as ``{{cookiecutter.project_name}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Usage

Generate a new SAM based Serverless App: `sam init --location gh:GonzalezAndrew/cookiecutter-aws-sam-python`

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

## Options

The following are the options which cookiecutter will prompt you when using this cookiecutter template.

| Option             | Description                                              | Default        |
|--------------------|----------------------------------------------------------|----------------|
| **project_name**   | The name of the lambda project.                          | `hello_world`  |
| **lambda_name**    | The name of the lambda function.                         | `HelloWorld`   |
| **python_version** | The version of Python to be used by the Lambda Function. | `3.9`          |
| **author**         | The author of the lambda function.                       | `foo`          |
| **email**          | The authors email address.                               | `foo@fuzz.com` |
