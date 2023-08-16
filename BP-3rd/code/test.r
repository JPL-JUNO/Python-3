1 + 2
add <- function(x, y) {
    x + y
}
print(add(1, 2))
h <- c(1, 2, 3, 4, 5, 6)
M <- c("A", "B", "C", "D", "E", "F")
barplot(h,
    names.arg = M, xlab = "X", ylab = "Y",
    col = "#00cec9", main = "Chart", border = "#fdcb6e"
)

library(ggplot2)
ggplot(mpg, aes(displ, hwy, color = class)) +
    geom_point()

2 + 3
a <- c(1, 2, 4)

print(a)
