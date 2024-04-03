terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(TF_VAR_SERVICE_ACCOUNT_FILE)
  project     = TF_VAR_GCP_PROJECT_ID
  region      = TF_VAR_REGION
}


resource "google_storage_bucket" TF_VAR_STORAGE_BUCKET_NAME {
  name          = TF_VAR_STORAGE_BUCKET_NAME
  location      = TF_VAR_LOCATION
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}



resource "google_bigquery_dataset" TF_VAR_BQ_DATASET_NAME {
  dataset_id = TF_VAR_BQ_DATASET_NAME
  location   = TF_VAR_LOCATION
}