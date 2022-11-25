function test(x) {
    if (x == 69) {
        throw 'thx';
    }
    try {
        x = 2;
    } finally {
        a = 2;
    }
}