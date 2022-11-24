function testhrowtrycatchfinally(x) {
    if (x == 69) {
        throw 'throw';
    }
    try {
        try {
            fungsigajelas(x);
        }
        finally {
            tubesgajelas(x);
        }
    }
    catch {
        return x;
    }
}