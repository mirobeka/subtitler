from urllib2 import urlopen, URLError, HTTPError

# few mother fucking constants
BASE_DOWNLOAD_DIRECTORY = './down/'
BASE_DOWNLOAD_URL = 'http://dl.opensubtitles.org/en/download/sub/'
MAX_COUNT = 10

# set apropriate value if you want to use mother fucking file with urls
# TODO: something is wrong with using this, I don't recommend
USE_URL_FILE = False

def dl_zip(url):
  try:
    # open mother fucking url
    remote = urlopen(url)

    # print mother fucking message
    print "downloading "

    # check if we have actual zip file.
    if 'zip' not in remote.info()['content-type']:
      # screw this...
      print 'zip file not found on this url \n\t' + url
      return False

    # create mother fucking file name
    local_file_name = url.split('/').pop()+'.zip'
    with open(BASE_DOWNLOAD_DIRECTORY + local_file_name, 'wb') as local_file:
      # TODO: extract just mother fucking subtitles from mother fucking zip file

      # save this mother fucking file
      local_file.write(remote.read())

  except HTTPError, e:
    print "Mother fucking HTTP error " + e
  except URLError, e:
    print "Mother fucking URL error " + e

  # everything went well, we have zip file downloaded
  print 'got you bitch! \n\t' + url
  return True

def give_me_permutations():
  # don't look for elegance, this is not priority :D
  letters = list('01234456789')
  mf_perm = ['469'+a+b+c+d for a in letters for b in letters for c in letters for d in letters for e in letters]
  return mf_perm

def trial_error(ulfl = []):
  # If we have some usefull information from previous tries, like correct urls, we can use those mother fucking urls
  usefull_list_for_later = ulfl

  for url in usefull_list_for_later:
    dl_zip(url)

  # prepare all mother fucking url endings   http://dl.open ... /sub/*******
  permutations = give_me_permutations()

  # it's 3am, I don't have time to write nice code...
  index = 0
  count = 0
  while count < MAX_COUNT:
    file_url = BASE_DOWNLOAD_URL + permutations[index]
    if file_url not in usefull_list_for_later:
      if dl_zip(file_url):
        usefull_list_for_later.append(file_url)
        count += 1
    index += 1
  
  return usefull_list_for_later

def load_usefull_list():
  if not os.path.isfile('urls.txt'):
    # I know, stupid
    f = open('urls.txt','wb')
    f.close()
  return [url for url in open('urls.txt','r').readlines()]

def save_usefull_list(ulfl):
  with open('urls.txt','wb') as f:
    for url in ulfl:
      f.write(url + '\n')

if __name__ == '__main__':
  ulfl = [] 
  if USE_URL_FILE:
    ulfl = load_usefull_list()
  extended_list = trial_error(ulfl)
  save_usefull_list(extended_list)

