import requests
from bs4 import BeautifulSoup
from PIL import Image
from tqdm import tqdm

# code by github.com/Vinay26k

def downloadSlides(BASE_URL, pdf_file_name=None):
    """This function downloads the slides from Slidershare.net url

    Args:
        BASE_URL ([str]): URL pointing to slideshare presentation/ slides
    """""
    # get content
    data = requests.get(BASE_URL).content
    # parse it with soup
    soup = BeautifulSoup(data, features="html.parser")
    # get slide containers
    slide_container = soup.find("div", attrs={"class":"slide_container"})
    # get image components
    slide_section_images = slide_container.findAll("img", attrs={"class":"slide_image"})
    # get all images links
    images_links_list = [x.get('data-full', "Some Issue Occured") for x in slide_section_images]
    # generate file name based on URL if not passed as param
    pdf_file_name = '_'.join(BASE_URL.split("/")[-2:])+".pdf" if not pdf_file_name else pdf_file_name.replace(".pdf","")+".pdf"
    # stream images from url and create them Image objects
    images_list = [Image.open(requests.get(images_links_list[each_image_index], stream=True).raw) for each_image_index in tqdm(range(len(images_links_list)))]
    # append all images to PDF file
    images_list[0].save(pdf_file_name, "PDF", resolution=100.0, save_all=True, append_images=images_list[1:])
    # return filename
    return pdf_file_name