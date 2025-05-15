{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "907d5445-9c8c-4726-b205-13a66d30a09e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Azure Blob Storage mounted successfully!\n"
     ]
    },
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr><th>path</th><th>name</th><th>size</th><th>modificationTime</th></tr></thead><tbody><tr><td>dbfs:/mnt/olympicdb123/dictionary.csv</td><td>dictionary.csv</td><td>7624</td><td>1742460282000</td></tr><tr><td>dbfs:/mnt/olympicdb123/summer.csv</td><td>summer.csv</td><td>2573921</td><td>1742460283000</td></tr><tr><td>dbfs:/mnt/olympicdb123/winter.csv</td><td>winter.csv</td><td>466225</td><td>1742460282000</td></tr></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [
        [
         "dbfs:/mnt/olympicdb123/dictionary.csv",
         "dictionary.csv",
         7624,
         1742460282000
        ],
        [
         "dbfs:/mnt/olympicdb123/summer.csv",
         "summer.csv",
         2573921,
         1742460283000
        ],
        [
         "dbfs:/mnt/olympicdb123/winter.csv",
         "winter.csv",
         466225,
         1742460282000
        ]
       ],
       "datasetInfos": [],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {},
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [
        {
         "metadata": "{}",
         "name": "path",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "name",
         "type": "\"string\""
        },
        {
         "metadata": "{}",
         "name": "size",
         "type": "\"long\""
        },
        {
         "metadata": "{}",
         "name": "modificationTime",
         "type": "\"long\""
        }
       ],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Define Azure Storage details\n",
    "storage_account_name = \"kushmi123\"  # Azure Storage Account Name\n",
    "sas_token = \"sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-03-20T17:02:10Z&st=2025-03-20T09:02:10Z&spr=https&sig=PM%2BmM3L98smfzDvaKtbrfmcpuZSdFb0wBTJikvKIn5Q%3D\"  # Your SAS Token\n",
    "container_name = \"olympicdb123\"  # Container name\n",
    "mount_point = f\"/mnt/{container_name}\"  # Mount location in Databricks\n",
    "\n",
    "# Unmount if already mounted\n",
    "if any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):\n",
    "    dbutils.fs.unmount(mount_point)\n",
    "\n",
    "# Mount the Blob Storage using SAS Token\n",
    "configs = {f\"fs.azure.sas.{container_name}.{storage_account_name}.blob.core.windows.net\": sas_token}\n",
    "dbutils.fs.mount(\n",
    "    source=f\"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/\",\n",
    "    mount_point=mount_point,\n",
    "    extra_configs=configs\n",
    ")\n",
    "\n",
    "print(\"Azure Blob Storage mounted successfully!\")\n",
    "\n",
    "# Verify mount by listing files\n",
    "display(dbutils.fs.ls(mount_point))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "613a6bb3-d6bd-4064-a8d0-69d9c054f50f",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Schema for dictionary:\nroot\n |-- Country: string (nullable = true)\n |-- Code: string (nullable = true)\n |-- Population: integer (nullable = true)\n |-- GDP_per_Capita: double (nullable = true)\n\nTable 'bronze_dictionary' loaded successfully.\nSchema for summer:\nroot\n |-- Year: integer (nullable = true)\n |-- City: string (nullable = true)\n |-- Sport: string (nullable = true)\n |-- Discipline: string (nullable = true)\n |-- Athlete: string (nullable = true)\n |-- Country: string (nullable = true)\n |-- Gender: string (nullable = true)\n |-- Event: string (nullable = true)\n |-- Medal: string (nullable = true)\n\nTable 'bronze_summer' loaded successfully.\nSchema for winter:\nroot\n |-- Year: integer (nullable = true)\n |-- City: string (nullable = true)\n |-- Sport: string (nullable = true)\n |-- Discipline: string (nullable = true)\n |-- Athlete: string (nullable = true)\n |-- Country: string (nullable = true)\n |-- Gender: string (nullable = true)\n |-- Event: string (nullable = true)\n |-- Medal: string (nullable = true)\n\nTable 'bronze_winter' loaded successfully.\n+----+------+--------+----------+--------------------+-------+------+--------------------+------+\n|Year|  City|   Sport|Discipline|             Athlete|Country|Gender|               Event| Medal|\n+----+------+--------+----------+--------------------+-------+------+--------------------+------+\n|1896|Athens|Aquatics|  Swimming|       HAJOS, Alfred|    HUN|   Men|      100M Freestyle|  Gold|\n|1896|Athens|Aquatics|  Swimming|    HERSCHMANN, Otto|    AUT|   Men|      100M Freestyle|Silver|\n|1896|Athens|Aquatics|  Swimming|   DRIVAS, Dimitrios|    GRE|   Men|100M Freestyle Fo...|Bronze|\n|1896|Athens|Aquatics|  Swimming|  MALOKINIS, Ioannis|    GRE|   Men|100M Freestyle Fo...|  Gold|\n|1896|Athens|Aquatics|  Swimming|  CHASAPIS, Spiridon|    GRE|   Men|100M Freestyle Fo...|Silver|\n|1896|Athens|Aquatics|  Swimming|CHOROPHAS, Efstat...|    GRE|   Men|     1200M Freestyle|Bronze|\n|1896|Athens|Aquatics|  Swimming|       HAJOS, Alfred|    HUN|   Men|     1200M Freestyle|  Gold|\n|1896|Athens|Aquatics|  Swimming|    ANDREOU, Joannis|    GRE|   Men|     1200M Freestyle|Silver|\n|1896|Athens|Aquatics|  Swimming|CHOROPHAS, Efstat...|    GRE|   Men|      400M Freestyle|Bronze|\n|1896|Athens|Aquatics|  Swimming|       NEUMANN, Paul|    AUT|   Men|      400M Freestyle|  Gold|\n+----+------+--------+----------+--------------------+-------+------+--------------------+------+\n\n+----+--------+--------+----------+--------------------+-------+------+---------------+------+\n|Year|    City|   Sport|Discipline|             Athlete|Country|Gender|          Event| Medal|\n+----+--------+--------+----------+--------------------+-------+------+---------------+------+\n|1924|Chamonix|Biathlon|  Biathlon|         BERTHET, G.|    FRA|   Men|Military Patrol|Bronze|\n|1924|Chamonix|Biathlon|  Biathlon|      MANDRILLON, C.|    FRA|   Men|Military Patrol|Bronze|\n|1924|Chamonix|Biathlon|  Biathlon| MANDRILLON, Maurice|    FRA|   Men|Military Patrol|Bronze|\n|1924|Chamonix|Biathlon|  Biathlon|     VANDELLE, André|    FRA|   Men|Military Patrol|Bronze|\n|1924|Chamonix|Biathlon|  Biathlon|AUFDENBLATTEN, Adolf|    SUI|   Men|Military Patrol|  Gold|\n|1924|Chamonix|Biathlon|  Biathlon|     JULEN, Alphonse|    SUI|   Men|Military Patrol|  Gold|\n|1924|Chamonix|Biathlon|  Biathlon|         JULEN, Ant.|    SUI|   Men|Military Patrol|  Gold|\n|1924|Chamonix|Biathlon|  Biathlon|         VAUCHER, D.|    SUI|   Men|Military Patrol|  Gold|\n|1924|Chamonix|Biathlon|  Biathlon|        BREMER, V.E.|    FIN|   Men|Military Patrol|Silver|\n|1924|Chamonix|Biathlon|  Biathlon|       ESKELINEN, A.|    FIN|   Men|Military Patrol|Silver|\n+----+--------+--------+----------+--------------------+-------+------+---------------+------+\n\n+-------------------+----+----------+----------------+\n|            Country|Code|Population|  GDP_per_Capita|\n+-------------------+----+----------+----------------+\n|        Afghanistan| AFG|  32526562|594.323081219966|\n|            Albania| ALB|   2889167|3945.21758150914|\n|            Algeria| ALG|  39666519|4206.03123244958|\n|    American Samoa*| ASA|     55538|            NULL|\n|            Andorra| AND|     70473|            NULL|\n|             Angola| ANG|  25021974|4101.47215182964|\n|Antigua and Barbuda| ANT|     91818|13714.7319616988|\n|          Argentina| ARG|  43416755|13431.8783398577|\n|            Armenia| ARM|   3017712|3489.12768956995|\n|             Aruba*| ARU|    103889|            NULL|\n+-------------------+----+----------+----------------+\n\n"
     ]
    }
   ],
   "source": [
    "# Define Bronze layer file paths (pointing to actual DBFS location)\n",
    "file_paths = {\n",
    "    \"dictionary\": \"dbfs:/mnt/olympicdb123/dictionary.csv\",\n",
    "    \"summer\": \"dbfs:/mnt/olympicdb123/summer.csv\",\n",
    "    \"winter\": \"dbfs:/mnt/olympicdb123/winter.csv\"\n",
    "}\n",
    "\n",
    "# Load and store data in Delta format for Bronze Layer\n",
    "for table, path in file_paths.items():\n",
    "    try:\n",
    "        # Read CSV with schema inference\n",
    "        df = spark.read.csv(path, header=True, inferSchema=True)\n",
    "\n",
    "        # Rename columns safely by replacing spaces with underscores\n",
    "        column_names = [c.replace(\" \", \"_\") for c in df.columns]\n",
    "        df = df.toDF(*column_names)\n",
    "        \n",
    "        # Print schema for debugging\n",
    "        print(f\"Schema for {table}:\")\n",
    "        df.printSchema()\n",
    "        \n",
    "        # Store as Delta Table in Bronze Layer (ensuring unique table names)\n",
    "        bronze_table_name = f\"bronze_{table}\"\n",
    "        df.write.format(\"delta\").mode(\"overwrite\").saveAsTable(bronze_table_name)\n",
    "\n",
    "        print(f\"Table '{bronze_table_name}' loaded successfully.\")\n",
    "\n",
    "    except Exception as e:\n",
    "        print(f\"Error loading {table}: {str(e)}\")\n",
    "\n",
    "# Verify the ingested data\n",
    "spark.sql(\"SELECT * FROM bronze_summer LIMIT 10\").show()\n",
    "spark.sql(\"SELECT * FROM bronze_winter LIMIT 10\").show()\n",
    "spark.sql(\"SELECT * FROM bronze_dictionary LIMIT 10\").show()\n"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "2"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": -1,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "O_Bronze",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}