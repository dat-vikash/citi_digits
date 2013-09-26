__author__ = 'vikash'

from django import template

register = template.Library()

def roundToHalf(number):
    """
    This will round to the nearest .5
    """
    convertedNumber = float(number)
    decimalNumber = (convertedNumber - int(convertedNumber))
    decimalNumber = round(decimalNumber * 10)
    if decimalNumber == 5:
        return int(convertedNumber) + .5
    if decimalNumber < 3 or decimalNumber > 7 :
        return round(convertedNumber)
    else:
        return int(convertedNumber) + .5


register.filter('roundToHalf', roundToHalf)
