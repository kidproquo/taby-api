date=$(date '+%Y-%m-%d-%H-%M-%S')

docker build -t repo.treescale.com/kidproquo/taby-api:$date .

# docker push repo.treescale.com/kidproquo/taby-api:$date