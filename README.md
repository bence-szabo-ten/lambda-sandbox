## Build & run
```
docker build -t priceless-scraper:latest .
docker run --rm -p 9000:8080 priceless-scraper:latest
```

## Test

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}
```