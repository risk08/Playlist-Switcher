import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
yt_service.ssl = True

yt_service.developer_key = 'AIzaSyCl4GSLMM5446DAF-9KVPBnULiIWldCsew'
yt_service.client_id = '6546054084-0dhu8h54cknvsqcf7ea2cpog9cjl9ki1.apps.googleusercontent.com'

def GetAuthSubUrl():
    next = 'http://www.example.com/video_upload.pyc'
    scope = 'http://gdata.youtube.com'
    secure = False
    session = True
    yt_service = gdata.youtube.service.YouTubeService()
    return yt_service.GenerateAuthSubURL(next, scope, secure, session)

authSubUrl = GetAuthSubUrl()
print authSubUrl