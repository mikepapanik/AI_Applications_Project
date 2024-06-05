import numpy
import functools
import operator

def img2chromosome(img_arr):
    """
     Αντιπροσωπεύει την εικόνα ως 1D διάνυσμα.
     img_arr: Η εικόνα που πρόκειται να μετατραπεί σε διάνυσμα.
     Επιστρέφει το διάνυσμα.
    """

    return numpy.reshape(a=img_arr, newshape=(functools.reduce(operator.mul, img_arr.shape)))

def chromosome2img(vector, shape):
    """
    Μετατρέπει ένα διάνυσμα 1D σε πίνακα.
    διάνυσμα: Το διάνυσμα που πρόκειται να μετατραπεί σε πίνακα.
    σχήμα: Το σχήμα του πίνακα στόχου.
    Επιστρέφει τον πίνακα.
    """

    # Ελέγξτε εάν το διάνυσμα μπορεί να αναδιαμορφωθεί σύμφωνα με το καθορισμένο σχήμα.
    if len(vector) != functools.reduce(operator.mul, shape):
        raise ValueError("A vector of length {vector_length} into an array of shape {shape}.".format(vector_length=len(vector), shape=shape))

    return numpy.reshape(a=vector, newshape=shape)
