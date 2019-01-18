from __future__ import absolute_import
from .transformer import Transformer
from .detection import detectBoxes
from ..techniques.technique import PositionVariantTechnique



class TransformerForImageDetection(Transformer):

    def __init__(self,technique,dictLabels=None):
        Transformer.__init__(self,technique,dictLabels)

    def transform(self, image, boxes):
        newImage = self.technique.apply(image)

        if (isinstance(self.technique, PositionVariantTechnique)):
            newBoxes = detectBoxes(image, boxes, self.technique)
            newBoxes = [(self.transformLabel(box[0]),box[1]) for box in newBoxes]
        else:
            newBoxes= [(self.transformLabel(box[0]),box[1]) for box in boxes]

        return [newImage,newBoxes]