# Python API trace using the Datadog Lambda Library

This project is a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework. Also integrates the Datadog the APM spans.

You can find the orginal template in the [Serverless Examples Repo](https://github.com/serverless/examples/tree/v3/aws-python-http-api). This project was based on a [MacSantos](https://github.com/mecsantos)' project.

## Prerequisites
- Access to your Datadog's Account
- Access to your AWS Account via CLI
- npm, yarn commands
- Serverless Framework CLI version 3. See [Serverless Framework docs](https://www.serverless.com/framework/docs/getting-started/)


## Usage

### Configuration
Fill in YOUR DATADOG API KEY, YOUR AWS PROFILE, YOUR NAME in the `serverless.yml` file.


### Deployment

Install the serverless-plugin-datadog:
```
$ cd python-serverless-api
$ npm install
```

Deploy the serverless stack:
```
$ serverless deploy
```

After deploying, you should see output similar to:
```bash
Deploying python-serverless-api to stage dev (us-east-1)

✔ Service deployed to stack python-serverless-api-dev (140s)

endpoint: GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
functions:
  hello: python-serverless-api-project-dev-hello (2.3 kB)
```

### Invocation

After successful deployment, you can call the created application via HTTP:

```
https://xxxxxxx.execute-api.us-east-1.amazonaws.com/
```

### Clean up

Delete the serverless stack:
```
$ serverless remove
```
