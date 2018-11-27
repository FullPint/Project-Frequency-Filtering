import numpy as np

class FFT_DIP:
    def fft(self, vector):
        vector = np.array(vector, dtype=complex)
        n = vector.shape[0]
        if(self._power_of_two(n)):
            vector = self.cooleytukey(vector)
        else:
            vector = np.fft.fft(vector)
            # vector = self.bluestein(vector)
        return vector

    def ifft(self, vector):
        vector = np.array(vector, dtype=complex)
        n = vector.shape[0]
        if(self._power_of_two(n)):
            vector = self.cooleytukey(vector, inverse=True)
        else:
            vector = np.fft.ifft(vector)
            """
            # need to completr the algorithm
            vector = self.bluestein(vector, inverse=True)
            """
        return vector.astype(int)

    def fft2d(self, matrix):
        matrix = np.apply_along_axis(self.fft, axis=1, arr=matrix)
        matrix = np.apply_along_axis(self.fft, axis=0, arr=matrix)
        return matrix

    def ifft2d(self, matrix):
        matrix = np.apply_along_axis(self.ifft, axis=1, arr=matrix)
        matrix = np.apply_along_axis(self.ifft, axis=0, arr=matrix)
        return matrix

    def fftshift(self, arr):
        # multi axis circle shifting
        arr = np.asarray(arr)
        num_axes = tuple(range(arr.ndim))
        axis_shifter = [arr.shape[i]//2 for i in num_axes]
        return np.roll(arr, axis_shifter, num_axes)

    def fftunshift(self, arr):
        # multi axis circle un-shifting
        arr = np.asarray(arr)
        num_axes = tuple(range(arr.ndim))
        axis_shifter = [-(arr.shape[i]//2) for i in num_axes]
        return roll(arr, axis_shifter, num_axes)

    def cooleytukey(self, vector, inverse=False):
        imaginary_factor = -2j if inverse == False else 2j
        vector = np.array(vector)
        N = np.int(vector.shape[0])
        if N <= 1:
            return vector
        even_fft = cooleytukey(vector[0::2])
        odd_fft =  cooleytukey(vector[1::2])
        tp = self._get_twiddle_product(N, odd_fft, inverse)
        transformed = [even_fft[i] + tp[i] for i in range(N//2)] + [even_fft[i] - tp[i] for i in range(N//2)]
        return np.asarray(transformed)

    """
    need to complete the implementation having issues with
    how to keep size, in order to avoid zero padding
    def bluestein(self, vector, inverse=False):

        transformed_vector = np.covolve()
        return vector
    """

    def _power_of_two(self, n):
        return (n > 0 and n & (n - 1) == 0)

    def _get_twiddle_product(self, n, odd_half, inverse=False):
        imag_coeff = -2j if inverse == False else 2j
        return [np.exp(imag_coeff*np.pi*i/n)*odd_half[i] for i in range(n//2)]
