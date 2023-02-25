# BGP Router

Made by Ha Ngo and Robert Rosas.

## High Level Approach

We didn't have a very complex high level approach. We essentially followed the recommended implementation plan, which was just getting our code to pass the tests in order. The starter code was extremely helpful to us, as Python is neither of our main languages and it set us out on a good direction, allowing us to focus more on BGP routing than attempting to understand the simulator.

Our process was:

1. Make feature
2. Test it on the next failing test cases
3. Make it work
4. See how many new tests it passes
5. Repeat

## Challenges

Our first challenge was running the simulator. Both of us have Windows machines and could not run it at first. Getting the simulator to run was definitely the hardest and most frustrating task, but we learned how to use the Khoury VMs, as well as how to install WSL so that we could run the simulator on our own machines.

Our next challenge after that was figuring out the structure of the data and how the starter code works. It took us a bit of time to figure out what socket.select does and where we should even begin running our program, but this did not take as long as running the simulator.

Afterwards, most of the journey was smooth sailing. While our code wouldn't work the first time we'd write it, the simulator logs were extremely helpful in figuring out where our router went wrong, as well as how we should fix it. However, the final callenge -- disaggregation -- was definitely the most difficult. We probably spent an hour just trying to figure out the process/math behind disaggregation, and another half an hour implementing it. It was very rewarding though to watch it succeed, and we're happy with our implementation (see the next section.)

## Cool design properties/features

* While it might not be the most efficient way of getting forwarding table entries, we realized that Python's given sorting algorithm is stable, so instead of writing a clunky comparison method to sort through the best match in our forwarding able, we instead had our program sort the data multiple times, one property at a time. It was a lot easier to implement and reason through than if we had used if/elif statements.
* Our aggregation/disaggregation methods are recursive and mirror each other very nicely. It felt very fundies-2-esque, and while figuring out how to perform aggregation/disaggregation was difficult, it makes a lot of sense to see the result in a recursive form.

## Testing

Our testing was very basic. We would run the simulator to see if our code passes; if it didn't, we would dot our code with prints to stderr in order to figure out what went wrong (since stdout doesn't seem to work with the simulator.)
