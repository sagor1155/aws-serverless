# aws-serverless
AWS With Serverless Framework

## lambda invoke
```bash
# With event file
sls invoke -f functionName -p path/of/event-json/file
# With data
sls invoke -f create -d '{"body":"Some meaningless data"}'
```

## lambda invoke local
```bash
# With event file
sls invoke local -f functionName -p path/of/event-json/file
# With data
sls invoke local -f create -d '{"body":"Some meaningless data"}'
```

## lambda deploy
```bash
sls deploy --verbose
sls deploy --stage stage-name --region region-name --function function-name --verbose
```

## generate event
```bash
sls generate-event -t aws:apiGateway > test-event.json
```

## display information about deployed service
```bash
sls info
``` 

## package your entire infrastructure
```bash
sls package
```