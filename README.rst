Formula One Module Repository
========================

This Ptyhon project downloads and prepares formula one data from the API ergast.com.



## Konfiguration

Erstellen Sie eine `config.json` Datei im Stammverzeichnis des Projekts. Verwenden Sie die `config_example.json` Datei als Vorlage. Die `config.json` Datei sollte die folgenden Informationen enthalten:

```json
{
  "aws_access_key_id": "YOUR_ACCESS_KEY",
  "aws_secret_access_key": "YOUR_SECRET_KEY",
  "region_name": "us-west-2",
  "table_name": "YOUR_TABLE_NAME"
}
