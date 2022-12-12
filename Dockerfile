FROM python:3.7

# Copy the Python script into the image
COPY merge_sorted_arrays.py /

# Set the entrypoint of the image to the Python script
ENTRYPOINT ["python", "/merge_sorted_arrays.py"]
