# wget https://github.com/gebart/python-v4l2capture
# ./setup.py build
# ./setup.py install
# sudo apt-get install python-imaging
# pip install imagae
# pip install PIL
import Image
import select
import v4l2capture
#TRY1--To resolve broken pipe error but it didn't work
#import signal

#-----TRY2--To resolve broken pipe error but it didn't work
#from signal import signal, SIGPIPE, SIG_DFL

# Open the video device.
video = v4l2capture.Video_device("/dev/video0")

# Suggest an image size to the device. The device may choose and
# return another size if it doesn't support the suggested one.
size_x, size_y = video.set_format(1280, 1024)

# Create a buffer to store image data in. This must be done before
# calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# raises IOError.
video.create_buffers(1)

# Send the buffer to the device. Some devices require this to be done
# before calling 'start'.
video.queue_all_buffers()

# Start the device. This lights the LED if it's a camera that has one.
video.start()

# Wait for the device to fill the buffer.
select.select((video,), (), ())

# The rest is easy :-)
image_data = video.read()
video.close()

#TRY1--To resolve the broken pipe this was added but didn,t work
signal.signal(signal.SIGPIPE, signal.SIG_DFL)


#-----TRY2--To resolve broken pipe error but it didn't work
#signal(SIGPIPE, SIG_DFL) 

#fromstring is removed and frombyte is added by sandeep team
image = Image.frombytes("RGB", (size_x, size_y), image_data)
#image = Image.fromstring("RGB", (size_x, size_y), image_data)
image.save("image.jpg")
iprint "Saved image.jpg (Size: " + str(size_x) + " x " + str(size_y) + ")"





##########################
#used this code to solve the broken pipe error but actual code was giving the indentation error for import Image

#from functools import wraps
#from sys import exit, stderr, stdout
#from traceback import print_exc


#def suppress_broken_pipe_msg(f):
#    @wraps(f)
#    def wrapper(*args, **kwargs):
#        try:
#            return f(*args, **kwargs)
#        except SystemExit:
#            raise
#        except:
#            print_exc()
#            exit(1)
#        finally:
#            try:
#                stdout.flush()
#            finally:
#                try:
#                    stdout.close()
#                finally:
#                    try:
#                        stderr.flush()
#                    finally:
#                        stderr.close()
#    return wrapper


#@suppress_broken_pipe_msg
#def main():
#    YOUR CODE GOES HERE
