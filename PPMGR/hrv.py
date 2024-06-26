import numpy as np



def mean_rr(rr_intervals):
    """Mean RR interval """
    return np.mean(rr_intervals)


def sdrr(rr_intervals):
    """Standard deviation of RR intervals"""
    return np.std(rr_intervals, ddof=1)


def sdsd(rr_intervals):
    """Standard deviation of differences between adjacent RR intervals """
    return np.std(np.diff(rr_intervals), ddof=1)


def rmssd(rr_intervals):
    """Root mean square of successive differences (rmssd)"""
    return np.sqrt(np.mean(np.diff(rr_intervals)**2))


def median_rr(rr_intervals):
    """Median RR interval (median_rr)"""
    return np.median(rr_intervals)


def range_rr(rr_intervals):
    """Range of RR intervals (range_rr)"""
    return np.max(rr_intervals) - np.min(rr_intervals)


def cvsd(rr_intervals):
    """Coefficient of variation of successive differences"""
    return rmssd(rr_intervals) / median_rr(rr_intervals)


def cvrr(rr_intervals):
    """Coefficient of variation of RR intervals"""
    return sdrr(rr_intervals) / median_rr(rr_intervals)


def hr(rr_intervals):
    """Heart rate (in beats per minute), calculated from RR intervals (in ms)"""
    return [60000 / rr for rr in rr_intervals]


def mean_hr(rr_intervals):
    """Mean heart rate (mean_hr)"""
    return np.mean(hr(rr_intervals))


def max_hr(rr_intervals):
    """Max heart rate"""
    return np.max(hr(rr_intervals))


def min_hr(rr_intervals):
    """Min heart rate"""
    return np.min(hr(rr_intervals))


def std_hr(rr_intervals):
    """Standard deviation of heart rate"""
    return np.std(hr(rr_intervals), ddof=1)


def calculate_parameters(rr_intervals):
    """Method that preforms calculation of all parameters on rr_intervals and return them in a dictionary"""
    return {
        'mean_rr': mean_rr(rr_intervals),
        'sdrr': sdrr(rr_intervals),
        'sdsd': sdsd(rr_intervals),
        'rmssd': rmssd(rr_intervals),
        "median_rr": median_rr(rr_intervals),
        "range_rr": range_rr(rr_intervals),
        "cvsd": cvsd(rr_intervals),
        "cvrr": cvrr(rr_intervals),
        "mean_hr": mean_hr(rr_intervals),
        "max_hr": max_hr(rr_intervals),
        "min_hr": min_hr(rr_intervals),
        "std_hr": std_hr(rr_intervals),
    }


def get_parameters(rr_intervals):
    """Method that prepares readable of calculate_parameters returned values version for display"""
    parameters=calculate_parameters(rr_intervals)
    parameters_for_display = {}
    for key, value in parameters.items():
        parameters_for_display[key] = round(float(value), 2)
    return parameters_for_display
