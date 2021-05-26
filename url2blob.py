from azure.storage.blob import BlobClient

accountURL = 'https://adlsbreakoutroom2.blob.core.windows.net/'
account_key = '0veYFcTs1570XMAOc7yNZOuDckYrgabjCCTldEevjS4hj24gvvM3t8qUzvAZHEREt3yMuqp4GDOWNGwFuSCcPg=='
container_name ='taxidata'
name = 'aug_uber_2014.csv'
link = 'https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/63bb878b76f47f69b4527d50af57aac26dead983/uber-trip-data/uber-raw-data-aug14.csv'

def run_sample(source = link):
    bc = BlobClient(account_url=accountURL, container_name=container_name, blob_name=name, snapshot=None, credential=account_key)
    bc.upload_blob_from_url(source_url=source, overwrite=False)

# Main method.
if __name__ == '__main__':
    run_sample()