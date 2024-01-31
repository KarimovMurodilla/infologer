#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  celery --app=utils.misc.celery_tasks.email_sender:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=utils.misc.celery_tasks.email_sender:celery flower
 fi