curl -X POST \
  https://api.fullcontact.com/v3/person.enrich \
  -H 'Authorization: Bearer fAm7gJcwpoemA1c287d7y8speAYslJ02'\
  -H "Content-Type: application/json" \
  -o "infos.json" \
  -d'{"emails":["bart@fullcontact.com","bart.lorang@fullcontact.com"]}'
