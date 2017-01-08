from rx import Observable

xs = Observable.from_(range(10))
d = xs.filter(
        lambda x: x % 2
    ).subscribe(print)