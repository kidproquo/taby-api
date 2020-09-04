date=$(date '+%Y-%m-%d-%H-%M-%S')

docker build -t repo.treescale.com/kidproquo/taby-pg-backup:$date .

docker push repo.treescale.com/kidproquo/taby-pg-backup:$date