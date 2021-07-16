
var width = device.width;
var height = device.height;

function get_screen_size() {
    return device.width, device.height;
}

function touch_promo() {
    screen_x_ercent = 0.9;
    screen_y_ercent = 0.92;
    run_tap(screen_x_ercent, screen_y_ercent);
}

function touch_consume() {
    toast("touch consume");
    let x1 = 0.3;
    let y1 = 0.3;
    run_tap(x1, y1);
    //    sleep(3000);

    let x2 = 0.5;
    let y2 = 0.4;
    run_tap(x2, y2);
    //   sleep(3000);

    let x3 = 0.8;
    let y3 = 0.4;
    run_tap(x3, y3);
    // sleep(3000);

    let x4 = 0.3;
    let y4 = 0.6;
    run_tap(x4, y4);


    let x5 = 0.5;
    let y5 = 0.6;
    run_tap(x5, y5);

    let x6 = 0.8;
    let y6 = 0.6;
    run_tap(x6, y6);

}
function run_tap(x, y) {
    x = width * x;
    y = height * y;
    x = x * (1 + Math.random() * 0.002);
    y = y * (1 + Math.random() * 0.002);
    toast(x);
    toast(y);
    click(x, y);
}

function clean_screen() {
    let x = 0.2;
    let y = 0.8;
    run_tap(x, y);

    x = 0.7;
    y = 0.65;
    run_tap(x, y);

    x = 0.5;
    y = 0.5;
    run_tap(x, y);

    x = 0.5;
    y = 0.65;
    run_tap(x, y);

    x = 0.15;
    y = 0.9;
    run_tap(x, y);

}

for (let count = 0; count < 5000; count++) {

    if (device.isScreenOn()) {

        touch_consume();
        clean_screen();
        for (let i = 0; i < 50; i++) {
            if (device.isScreenOn()) {
                touch_promo();
            }
            else {
                break;
            }
        }
    }
    else {
        break;
    }
}