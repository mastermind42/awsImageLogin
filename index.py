import boto3
import botocore
import os
import pylint

resource = boto3.resource('s3')
client = boto3.client('s3')
rekognition = boto3.client('rekognition')

"""
for bucket in s3.buckets.all():
    print(bucket.name)
"""

# Will create bucket if it doesn't exist.
def createBucket(bucketName):
	try:
		resource.meta.client.head_bucket(Bucket=bucketName)
	except botocore.exceptions.ClientError as e:
		error_code = int(e.response['Error']['Code'])
		if error_code == 404:
			resource.create_bucket(Bucket=bucketName, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
	
def getBucketTree(bucketName):
	bucket = resource.Bucket(bucketName)
	bucketList = list(bucket.objects.all())
	return bucketList
	#return list(map(lambda x: x.key, bucket.objects.all()))
'''	for item in bucket.objects.all():
		#bucketList.append(item.key.split('/'))
		bucketList.append(item)
	return bucketList'''

def getUserList(bucketName):
	bucketList = getBucketTree(bucketName)
	userList = [] # userList[0] = User's Name, userList[1] = list of all locations
	#for items in bucketList:
	#	if item.startswith('Users/'):

def uploadAndDelete(pathToDir, bucketName):
	# Uploads file to s3 bucket and deletes it
	for item in os.listdir(pathToDir):
		if item.endswith(".jpg"):
			fullFilePath = os.path.join(pathToDir, item)
			client.upload_file(fullFilePath, bucketName, item)
			os.remove(fullFilePath)

def isPicture(key):
	if(key.endswith('jpg') or key.endswith('jpeg')):
		return True
	else:
		return False

# filesToUpload = []
# Search for all files in pathToDir that ends with .jpg
#def uploadAndCompare(pathToDir, bucketName):
	'''
	Source = {
		'S3Object': {
			'Bucket': bucketName,
			'Name': item
		}
	}
	Destination = {
		'S3Object': {
			'Bucket': bucketName,
			'Name': item
		}
	}
	comp = client.compare_faces(SourceImage=Source, TargetImage=Destination, SimilarityThreshold=80)
	print(comp)'''


pathToDir = '/Users/rohitsaxena/GitProjects/similiarity-monitor/Pics'
bucketName = 'unknowns'
baseBucket = 'iot-proj'

# createBucket(baseBucket)
# createBucket(bucketName)
# uploadAndDelete(pathToDir, bucketName)

# Source is is the known pictures
# Destination is the unknown pictures
"""
for known in getBucketTree(baseBucket):
	if(isPicture(known.key) == False):
		print(known)

knownPictures = [][]
for known in getBucketTree(baseBucket):
	if(isPicture(known.key)):
"""

for known in getBucketTree(baseBucket):
	print(known.key)		


for unknown in getBucketTree(bucketName):
	for known in getBucketTree(baseBucket):
		if(isPicture(known.key)):			
			Source = {
				'S3Object': {
					'Bucket': baseBucket,
					'Name': known.key
				}
			}
			Destination = {
				'S3Object': {
					'Bucket': bucketName,
					'Name': unknown.key
				}
			}
			#print(Source)
			#print(Destination)
			comp = rekognition.compare_faces(SourceImage = Source, TargetImage= Destination, SimilarityThreshold=80)
			#comp = rekognition.compare_faces(SourceImage = known, TargetImage= unknown, SimilarityThreshold=80)
			if(len(comp['FaceMatches']) > 0):
				print('Matched:', unknown.key, 'matched with', known.key, 'of Confidence:', comp['FaceMatches'][0]['Face']['Confidence'], '%')
				break
			
			if(len(comp['UnmatchedFaces']) > 0):
				print('Not matched', unknown.key, 'not matched with', known.key, comp['UnmatchedFaces'][0]['Confidence'], '%')

			#print(comp)
	



tree = getBucketTree('iot-proj')
for ob in tree:
	#print(ob.key)
	print(ob)
	#print(ob.key.metadata['x-amz-meta-user'])

#print(tree.key.get_metadata('x-amz-meta-user'))