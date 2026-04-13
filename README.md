# WebScraper
## Project implementation steps
### Stages 1-3
1. Provide URL address of product's opinions webpage
2. Send the request to provided URL address
3. If status code is OK, fetch product name
4. If status code is OK, fetch all opinions from requested webpage
5. For all fetched opinions, parse them to extract relevant data
6. Check if there is next page with opinions
7. For all remaining pages repeat steps 2-5
8. Save obtained opinions

## Project inputs
### Product codes
- 55627202
- 83359249
- 167886083
- 174130671
- 34935197
- 8679864
- 105022684
### Opinion structure
|component|name|selector|
|---------|----|--------|
|opinion ID |opinion_id|[data-entry-id]|
|opinion’s author|author|span.user-post__author-name|
|author's recommendation|recommendation|span.user-post__author-recomedation > em|
|score expressed in number of start|score|span.user-post__score-count|
|opinions content|content|div.user-post__text|
|list of product advantages|pros|div.review-feature__item--positive|
|list of product disadvantages|cons|div.review-feature__item--negative|
|how many users think that opinion was helpful|like|button.vote-yes > span|
|how many users think that opinion was unhelpful|dislike|button.vote-no > span|
|publishing date|publish_date|user-post__published > time:nth-child(1)[datetime]|
|purchase date|purchase_date|user-post__published > time:nth-child(2)[datetime]|