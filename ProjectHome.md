The Shannon entropy is a measure of the amount of information, or uncertainty, in a given piece of data. The py-entropy library provides an easy way to compute this important metric.

### Basic usage ###

Use the `entropy` function in the `entropy` module.

```
>>> import entropy
>>> entropy.entropy("mystring")
3.0
>>> entropy.entropy("mystringisastring")
3.0574760762899316
>>> entropy.entropy("google")
1.9182958340544896
>>> entropy.entropy("snnsp3")
1.9182958340544896
```