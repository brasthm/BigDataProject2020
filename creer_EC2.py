import boto3


ec2 = boto3.resource('ec2')
ec2.create_instances(
    SecurityGroups = ["ssh"],
    ImageId='ami-00068cd7555f543d5',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='bigDataProject')



