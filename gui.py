from __future__ import print_function
from ipywidgets import *
from traitlets import Integer, HasTraits, link
from IPython.display import display
from reducer.image_browser import FitsViewer

from model import SourceDetection, AperturePhotometry

class FileSelect(Box):
    """
    Class that initialies a button and dropdown interface for the final
    GUI class.
    
    """
    def __init__(self, fileList = [0]):
        self._aButton = Dropdown(options = fileList,
                                 value = fileList[0],
                                 description = "Image")
        self._dropdown = Dropdown(options = fileList,
                     value = fileList[0],
                    description = "Method")
        super(FileSelect, self).__init__(children = [self._aButton, self._dropdown],
                                layout = Layout(display='flex',
                                                flex_flow='row',
                                                align_items='stretch',
                                                width='100%'))

class SettingSlider(Box):
    """
    Class that initalizes a linked slider and text entry interface for the final 
    GUI class. 
    
    """
    def __init__(self, d = 'Description',minimum = 0.0, maximum = 50.0):
        self._slide = FloatSlider(value = minimum,
                                 min = minimum,
                                 max = maximum,
                                 step = 0.1,
                                 description = d)
        self._text = BoundedFloatText(value = minimum,
                                             min = minimum,
                                             max = maximum)
        link((self._slide,'value'),(self._text,'value'))
        super(SettingSlider, self).__init__(children = [self._slide, self._text],
                                layout = Layout(display='flex',
                                                flex_flow='row',
                                                align_items='stretch',
                                                width='100%'))
class ImageViewer(Box):
    """
    Class that initalizes an image viewer interface for the final GUI
    class. 
    
    """
    def __init__(self,image_path):
        imageOpen = open(image_path,"rb")
        image = imageOpen.read()
        self._viewer = Image(value=image,format='jpg',width=600,height=400)
        super(ImageViewer, self).__init__(children = [self._viewer],
                                layout = Layout(display='flex',
                                                flex_flow='row',
                                                align_items='stretch',
                                                width='50%'))

class GUI(Box):
    """
    Class that combines the FileSelect, SettingSlider, and ImageViewer 
    interfaces into a cohesive GUI interface. 
    
    """
    def __init__(self, fileList, minimum, maximum,image_path):
        self.source_model = SourceDetection()
        self.phot_model = AperturePhotometry()
        
        self._file = FileSelect(fileList)
        self._view = ImageViewer(image_path)
        self._aperture = SettingSlider("Aperture (pixels)", minimum, maximum)
        self._gap = SettingSlider("Gap (pixels)", minimum, maximum)
        self._annulus = SettingSlider("Annulus (pixels)", minimum, maximum)
        self._go = Button(description = 'Go!')
        super(GUI, self).__init__(children = [self._file, self._view,
                                              self._aperture, self._gap,
                                              self._annulus, self._go],
                                            layout = Layout(display='flex',
                                                            flex_flow='column',
                                                            align_items='stretch',
                                                            width='50%'))
class TabGUI(Tab):
    """
    Class that puts GUIs into a tabbed interface. Will eventually be 
    implemented into the GUI class.
    """
    def __init__(self):
        self._firstTab = GUI(['Mal','Simon','River'],0.0,30.0,'images/1150228.jpg')
        self._secondTab = SettingSlider("Aperture", 2, 3)
        super(TabGUI,self).__init__(children = [self._firstTab, self._secondTab],
                                   _titles = {0:"First Method", 1:"Second Method"})
