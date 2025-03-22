#!/bin/bash

# Launch EC2 instance using AWS CLI
aws ec2 run-instances \
  --image-id ami-084568db4383264d4 \
  --instance-type t2.micro \
  --key-name my-key \
  --security-groups my-sg \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Auto,Value=Scaled}]' \
  --count 1
