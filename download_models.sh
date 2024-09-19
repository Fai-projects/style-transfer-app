BASE_URL="https://github.com/Walid-Ahmed/Neural-Style-Transfer-with-TF/raw/master/"

mkdir -p backend/models/temp
cd backend/models/temp
wget "$BASE_URL/models/candy.t7"
wget "$BASE_URL/models/la_muse.t7"
wget "$BASE_URL/models/mosaic.t7"
wget "$BASE_URL/models/feathers.t7"
wget "$BASE_URL/models/the_scream.t7"
wget "$BASE_URL/models/udnie.t7"