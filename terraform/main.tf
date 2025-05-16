provider "google" {
  project = "procurement-pipeline-demo"
  region  = "us-central1"
}

resource "google_storage_bucket" "procurement_data_bucket" {
  name     = "bucket-procurement-analytics"
  location = "US"
}

resource "google_bigquery_dataset" "procurement_dataset" {
  dataset_id                  = "procurement_analytics"
  location                    = "US"
  delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "procurement_assertions" {
  dataset_id                  = "procurement_analytics_assertions"
  location                    = "US"
  delete_contents_on_destroy = true
}