data<-read.csv("problemSet1.csv", header=TRUE)
plot(data$X, data$Y, xlab = "Cigarettes consumed per capita in 1930 (X)", ylab = "Lung cancer deaths per million people in 1950 (Y)", xlim = c(0, 1300), ylim=c(0, 500), main = "Regression of Lung cancer deaths on Cigarettes consumed per capita\nY = 28.3966 + 0.3364X")
par(new=TRUE)
curve(intercept+slope*x, col="red", ann = FALSE,  xlim = c(0, 1300), ylim=c(0, 500), lty=1, lwd = 3)
text(data$X, data$Y, data$Country, cex=0.7, pos=3, col="black")
legend("topleft", c("Regression line"), col = ("red"), bty='n', cex=.75, lty = c(1), lwd = c(3))