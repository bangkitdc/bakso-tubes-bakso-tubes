var x = 1;
switch (x) {
    case 0:
        x = x + 1;
        break;
    case 1:
        x = x;
    case null:
    default:
        x = x - 1;
}