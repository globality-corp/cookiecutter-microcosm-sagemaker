#!/bin/bash -e
# Name: rds_dump_to_s3.sh
#
# Purpose: Script to take database backup and push to s3.
#
#
apt update -qq > /dev/null 2> /dev/null
apt install -qq -y gnupg2 sudo jq wget curl unzip  > /dev/null 2> /dev/null
pip3 install --upgrade pip > /dev/null 2> /dev/null

mkdir ~/.gnupg
chmod 0700 ~/.gnupg
echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf
DB_USER=$ENV{NAME}
CURR_RELEASE=$ENV{NGINX_VERSION}
POSTGRES_DB_HOST="$ENV{${DB_USER}__POSTGRES__HOST}"

# Get debian version
RELEASE=`cat /etc/os-release|grep PRETTY_NAME|cut -d ' ' -f 4|tr -d '\(\)"'`
#Add postgres repo to get latest postgres packages
apt-key adv --fetch-keys http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc > /dev/null 2> /dev/null
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}-pgdg main" | sudo tee  /etc/apt/sources.list.d/pgdg.list
apt update -qq > /dev/null 2> /dev/null
apt install -qq -y postgresql-client  > /dev/null 2> /dev/null 
# Now install aws cli
curl "https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"    2> /dev/null
unzip -q awscliv2.zip  2> /dev/null
./aws/install  2> /dev/null
PGPASSWORD=`aws2 secretsmanager get-secret-value --secret-id secrets/dev2/${DB_USER} --version-stage ${CURR_RELEASE} | jq -r .SecretString | jq -r .config.postgres.password`

PGPASSWORD=$PGPASSWORD pg_dump --format custom --no-owner -x -U ${DB_USER} -h ${POSTGRES_DB_HOST} ${DB_USER}_db --compress 2 > /tmp/${DB_USER}.dump.$ENV{MICROCOSM_ENVIRONMENT}
aws2 s3 cp /tmp/${DB_USER}.dump.$ENV{MICROCOSM_ENVIRONMENT} s3://glob-db-dump-${MICROCOSM_ENVIRONMENT}/
exit 0
