require(ggpubr)
require(plyr)
require(tidyverse)

#### work direction ####
setwd("C:/Plos_data")

###### Load Data #####
# load and run vglut2 OR vgat seperately
#### vglut2 mice ###
pos<-read.csv(file = 'vglut2_mice.csv')

#### vgat mice ###
pos<-read.csv(file = 'vgat_mice.csv')



### name the channel
pos[which(pos$Ch == 1), "Ch"] <- "starter" #ch 1 is V5+ & RV_GFP+
pos[which(pos$Ch == 2), "Ch"] <- "vglut2" #ch 2 is RV_GFP+ & vgat-, V5-
pos[which(pos$Ch == 3), "Ch"] <- "vgat" #ch 3 is RV_GFP+ & vgat+, V5-

###
pos_a1<-pos[which(pos$mice == 'A1'),]
pos_a2<-pos[which(pos$mice == 'A2'),]
pos_a3<-pos[which(pos$mice == 'A3'),]


### count
as.data.frame(table(pos_a1$AP))
count(pos_a1, vars = c("AP", "Ch"))



### density plot, default: kernel = "gaussian", bw = "nrd0" #bw = bandwidth
##################################################################################################
###### density plot along A-P axis ######
# calculate mean density(normalized)
pa1 <- geom_line(aes(x = AP, after_stat(count/length(pos_a1[,1])), color = Ch), data = pos_a1, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.11)
pa2 <- geom_line(aes(x = AP, after_stat(count/length(pos_a2[,1])), color = Ch), data = pos_a2, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.11)
pa3 <- geom_line(aes(x = AP, after_stat(count/length(pos_a3[,1])), color = Ch), data = pos_a3, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.11)
da1 <- ggplot_build(ggplot()+pa1+xlim(c(-4.9, -3.2)))$data[[1]]
da2 <- ggplot_build(ggplot()+pa2+xlim(c(-4.9, -3.2)))$data[[1]]
da3 <- ggplot_build(ggplot()+pa3+xlim(c(-4.9, -3.2)))$data[[1]]
ave <- data.frame(x = da1$x, y = (da1$y+da2$y+da3$y)/3, Ch = rep(c("starter", "vgat", "vglut2"), each = length(da1[, 1])/3)) #rep(x, times, length.out, each)
#plot
ggplot()+
  pa1+
  pa2+
  pa3+
  geom_line(data = ave, aes(x = x, y = y, color = Ch), lwd = 0.8)+
  theme_classic() +
  scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  #ylim(c(0, 1.36))+
  scale_y_continuous(breaks = seq(0, 1.36, by = 0.3), limits = c(0, 1.36))+
  labs(y = "Density(normalized)")
ggsave("A-P density plot.pdf", width = 12, height = 7, units = "cm")

# ######## plot histogram and fitted normal curve
# pos_ap <- pos
# bw = 0.11
# pos_ap_fit <- pos_ap %>% # %>%: pipe, like convey x to f(x)
#   group_by(Ch, mice) %>%
#   summarise(mean = mean(AP), sd = sd(AP))
# write.csv(pos_ap_fit, "A-P Gaussian fit.csv")
# pos_ap %>%
#   group_by(Ch, mice) %>%
#   nest(data = c(ML, AP, DV, region)) %>%
#   mutate(y = map(data, ~ dnorm(
#     .$AP, mean = mean(.$AP), sd = sd(.$AP)
#   )*bw*sum(!is.na(.$AP)))) %>% # to rescale the normal curve to the histogram
#   unnest(c(data, y)) %>%
#   
#   ggplot(aes(x = AP, color = Ch, fill = Ch))+
#   geom_histogram(data = pos_ap, lwd = 0.6, binwidth = bw, alpha = 0.5) +
#   geom_line(aes(y = y), color = "black", lwd = 0.6) +
#   theme_classic() +
#   scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   facet_grid(rows = vars(Ch), cols = vars(mice)) +
#   #xlim(c(-1, 0.75))+
#   #ylim(c(0, 0.76))+
#   labs(y = "Counts", x = "AP")
# ggsave("A-P Gaussian fit.png", width = 20, height = 15, units = "cm")
# 
# ####### E/I of A-P ######
# #E/I
# n = length(da1$x)/3
# da1_ei <- data.frame(x = da1$x[1:n], y = da1$y[(2*n+1):(3*n)]/da1$y[(n+1):(2*n)])
# da2_ei <- data.frame(x = da1$x[1:n], y = da2$y[(2*n+1):(3*n)]/da2$y[(n+1):(2*n)])
# da3_ei <- data.frame(x = da1$x[1:n], y = da3$y[(2*n+1):(3*n)]/da3$y[(n+1):(2*n)])
# ave_ei <- data.frame(x = da1$x[1:n], y = (da1_ei$y+da2_ei$y+da3_ei$y)/3)
# #plot
# ggplot()+
#   geom_line(data = da1_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da2_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da3_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = ave_ei, aes(x = x, y = y), lwd = 0.8)+
#   theme_classic()+
#   scale_color_manual(values = "#383A3F")+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   labs(y = "E/I ratio", x = "AP")+
#   ylim(c(0, 1))
# ggsave("A-P E-I.pdf", width = 12, height = 5, units = "cm")
# write.csv(ave_ei, "A-P E-I.csv")


###################################################################################################
###### density plot along D-V axis ######
# at the central AP site, count and select the section with the most starters
# load and calculate one section from one animal and the corresponding template border coordinates one by one
# vglut2 mice #
pos_a1_dv <- pos_a1[which(pos_a1$AP == -3.86), ] # -3.86, -3.97, -4.08, tem38, 39, 40
pos_a2_dv <- pos_a2[which(pos_a2$AP == -3.75), ] # -3.75, -3.86, -3.97, tem37, 38, 39
pos_a3_dv <- pos_a3[which(pos_a3$AP == -3.74), ] # -3.74, -3.85, -3.96, tem37, 38, 39
# vgat mice #
pos_a1_dv <- pos_a1[which(pos_a1$AP == -4.01), ] # -3.79, -3.9, -4.01, tem37, 38, 39
pos_a2_dv <- pos_a2[which(pos_a2$AP == -3.85), ] # -3.63, -3.74, -3.85, tem35, 36, 37
pos_a3_dv <- pos_a3[which(pos_a3$AP == -4.08), ] # -3.86, -3.97, -4.08, tem38, 39, 40

## depth from the surface ##
# surface coordinates #
tem <- read.csv("template.csv")
tem <- transform.data.frame(tem)
tem38<-as.data.frame(spline(tem[which(tem$AP == -3.85), ]$ML, tem[which(tem$AP == -3.85), ]$DV, n = 2000))
tem38in <- abs((tem38[1, 1]-tem38[2, 1])/2) #calculate interval between dots
tem39<-as.data.frame(spline(tem[which(tem$AP == -3.95), ]$ML, tem[which(tem$AP == -3.95), ]$DV, n = 2000))
tem39in <- abs((tem39[1, 1]-tem39[2, 1])/2)
tem37<-as.data.frame(spline(tem[which(tem$AP == -3.75), ]$ML, tem[which(tem$AP == -3.75), ]$DV, n = 2000))
tem37in <- abs((tem37[1, 1]-tem37[2, 1])/2)
tem36<-as.data.frame(spline(tem[which(tem$AP == -3.65), ]$ML, tem[which(tem$AP == -3.65), ]$DV, n = 2000))
tem36in <- abs((tem36[1, 1]-tem36[2, 1])/2)
tem35<-as.data.frame(spline(tem[which(tem$AP == -3.55), ]$ML, tem[which(tem$AP == -3.55), ]$DV, n = 2000))
tem35in <- abs((tem35[1, 1]-tem35[2, 1])/2)
tem40<-as.data.frame(spline(tem[which(tem$AP == -4.05), ]$ML, tem[which(tem$AP == -4.05), ]$DV, n = 2000))
tem40in <- abs((tem40[1, 1]-tem40[2, 1])/2)
#ggplot(tem[which(tem$AP == -3.85), ], aes(x = ML, y = DV)) + geom_point()+ geom_line(data = tem38, aes(x = x, y = y))

### animals ###
# a1
tem_a1 <- tem38
tem_a1in <- tem38in
for (i in 1:length(pos_a1_dv[, 1])){
  for (j in 1:length(tem_a1[, 1])){
    if (abs(pos_a1_dv[i, 2]-tem_a1[j, 1])<tem_a1in){
      pos_a1_dv[i, 3] <- tem_a1[j, 2]-pos_a1_dv[i, 3]
      break
    }
  }
}
ram_a1 <- pos_a1_dv #1st
ram_a1 <- rbind(ram_a1, pos_a1_dv) #2nd, 3rd
pos_a1_dv <- ram_a1 #3rd
# a2
tem_a2 <- tem37
tem_a2in <- tem37in
for (i in 1:length(pos_a2_dv[, 1])){
  for (j in 1:length(tem_a2[, 1])){
    if (abs(pos_a2_dv[i, 2]-tem_a2[j, 1])<tem_a2in){
      pos_a2_dv[i, 3] <- tem_a2[j, 2]-pos_a2_dv[i, 3]
      break
    }
  }
}
ram_a2 <- pos_a2_dv #1st 
ram_a2 <- rbind(ram_a2, pos_a2_dv) #2nd, 3rd
pos_a2_dv <- ram_a2
# a3
tem_a3 <- tem37
tem_a3in <- tem37in
for (i in 1:length(pos_a3_dv[, 1])){
  for (j in 1:length(tem_a3[, 1])){
    if (abs(pos_a3_dv[i, 2]-tem_a3[j, 1])<tem_a3in){
      pos_a3_dv[i, 3] <- tem_a3[j, 2]-pos_a3_dv[i, 3]
      break
    }
  }
}
ram_a3 <- pos_a3_dv #1st
ram_a3 <- rbind(ram_a3, pos_a3_dv) #2nd, 3rd
pos_a3_dv <- ram_a3

# calculate mean density(normalized)
pa1_dv <- geom_line(aes(x = DV, after_stat(count/length(pos_a1_dv[,1])), color = Ch), data = pos_a1_dv, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
pa2_dv <- geom_line(aes(x = DV, after_stat(count/length(pos_a2_dv[,1])), color = Ch), data = pos_a2_dv, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
pa3_dv <- geom_line(aes(x = DV, after_stat(count/length(pos_a3_dv[,1])), color = Ch), data = pos_a3_dv, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
da1_dv <- ggplot_build(ggplot()+pa1_dv+xlim(c(0, 1.3)))$data[[1]]
da2_dv <- ggplot_build(ggplot()+pa2_dv+xlim(c(0, 1.3)))$data[[1]]
da3_dv <- ggplot_build(ggplot()+pa3_dv+xlim(c(0, 1.3)))$data[[1]]
ave_dv <- data.frame(x = da1_dv$x, y = (da1_dv$y+da2_dv$y+da3_dv$y)/3, Ch = rep(c("starter", "vgat", "vglut2"), each = length(da1_dv[, 1])/3)) #rep(x, times, length.out, each)
#plot
ggplot()+
  pa1_dv+
  pa2_dv+
  pa3_dv+
  geom_line(data = ave_dv, aes(x = x, y = y, color = Ch), lwd = 0.8)+
  theme_classic() +
  #scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+ #light yellow, blue, red
  scale_color_manual(values = c("#E3D25A", "#1E00DC", "#B80024"))+ #dark yellow, blue, red
  scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  xlim(c(0.6, 0))+
  scale_y_continuous(breaks = seq(0, 2, by = 0.5), limits = c(0, 2))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  coord_flip()+
  labs(y = "Density(normalized)", x = "Depth from SC surface")
ggsave("D-V density plot flipped.pdf", width = 10, height = 7, units = "cm") #10*7 or 12*7
write.csv(pos_a1_dv, "A1 depth.csv")
write.csv(pos_a2_dv, "A2 depth.csv")
write.csv(pos_a3_dv, "A3 depth.csv")

#
# pos_a1_dv <- read.csv("A1 depth.csv")
# pos_a2_dv <- read.csv("A2 depth.csv")
# pos_a3_dv <- read.csv("A3 depth.csv")


# ######## plot histogram and fitted normal curve
# pos_dv <- rbind(pos_a1_dv, pos_a2_dv, pos_a3_dv)
# bw = 0.11
# pos_dv_fit <- pos_dv %>% # %>%: pipe, like convey x to f(x)
#   group_by(Ch, mice) %>%
#   summarise(mean = mean(DV), sd = sd(DV))
# write.csv(pos_dv_fit, "D-V Gaussian fit.csv")
# pos_dv %>%
#   group_by(Ch, mice) %>%
#   nest(data = c(ML, AP, DV, region)) %>%
#   mutate(y = map(data, ~ dnorm(
#     .$DV, mean = mean(.$DV), sd = sd(.$DV)
#   )*bw*sum(!is.na(.$DV)))) %>% # to rescale the normal curve to the histogram
#   unnest(c(data, y)) %>%
#   
#   ggplot(aes(x = DV, color = Ch, fill = Ch))+
#   geom_histogram(data = pos_dv, lwd = 0.6, binwidth = bw, alpha = 0.5) +
#   geom_line(aes(y = y), color = "black", lwd = 0.6) +
#   theme_classic() +
#   scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   facet_grid(rows = vars(Ch), cols = vars(mice)) +
#   #xlim(c(-1, 0.75))+
#   #ylim(c(0, 0.76))+
#   labs(y = "Counts", x = "Depth from SC surface")
# ggsave("D-V Gaussian fit.png", width = 20, height = 15, units = "cm")
# 
# ####### E/I of D-V ######
# #E/I
# n = length(da1_dv$x)/3
# da1_dv_ei <- data.frame(x = da1_dv$x[1:n], y = da1_dv$y[(2*n+1):(3*n)]/da1_dv$y[(n+1):(2*n)])
# da2_dv_ei <- data.frame(x = da1_dv$x[1:n], y = da2_dv$y[(2*n+1):(3*n)]/da2_dv$y[(n+1):(2*n)])
# da3_dv_ei <- data.frame(x = da1_dv$x[1:n], y = da3_dv$y[(2*n+1):(3*n)]/da3_dv$y[(n+1):(2*n)])
# ave_dv_ei <- data.frame(x = da1_dv$x[1:n], y = (da1_dv_ei$y+da2_dv_ei$y+da3_dv_ei$y)/3)
# #plot
# ggplot()+
#   geom_line(data = da1_dv_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da2_dv_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da3_dv_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = ave_dv_ei, aes(x = x, y = y), lwd = 0.8)+
#   theme_classic()+
#   scale_color_manual(values = "#383A3F")+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   labs(y = "E/I ratio", x = "Depth from SC surface")+
#   ylim(c(0, 1))+
#   xlim(c(0, 0.6))
# ggsave("D-V E-I.pdf", width = 12, height = 5, units = "cm")
# ave_dv_ei <- ave_dv_ei[which(ave_dv_ei$x < 0.6), ]
# write.csv(ave_dv_ei, "D-V E-I.csv")


####################################################################################################
###### density plot along M-L axis ######
# at the central AP site, count and select the section with the most starters
# vglut2 mice #
pos_a1_ml <- pos_a1[which(pos_a1$AP == -4.08|pos_a1$AP == -3.97|pos_a1$AP == -3.86), ] # -3.86, -3.97, -4.08, tem38, 39, 40
pos_a2_ml <- pos_a2[which(pos_a2$AP == -3.86|pos_a2$AP == -3.97|pos_a2$AP == -3.75), ] # -3.75, -3.86, -3.97, tem37, 38, 39
pos_a3_ml <- pos_a3[which(pos_a3$AP == -3.96|pos_a3$AP == -3.85|pos_a3$AP == -3.74), ] # -3.74, -3.85, -3.96, tem37, 38, 39
# vgat mice #
pos_a1_ml <- pos_a1[which(pos_a1$AP == -3.79|pos_a1$AP == -3.9|pos_a1$AP == -4.01), ] # -3.79, -3.9, -4.01
pos_a2_ml <- pos_a2[which(pos_a2$AP == -3.85|pos_a2$AP == -3.74|pos_a2$AP == -3.63), ] # -3.63, -3.74, -3.85
pos_a3_ml <- pos_a3[which(pos_a3$AP == -4.08|pos_a3$AP == -3.97|pos_a3$AP == -3.86), ] # -3.86, -3.97, -4.08

# calculate kmeans of ML and use it as the center
# a1
ka1 = kmeans(pos_a1_ml[which(pos_a1_ml$Ch == "starter"), "ML"], 1, 25)
pos_a1_ml$ML <- pos_a1_ml$ML-ka1$centers[1, 1]

# a2
ka2 = kmeans(pos_a2_ml[which(pos_a2_ml$Ch == "starter"), "ML"], 1, 25)
pos_a2_ml$ML <- pos_a2_ml$ML-ka2$centers[1, 1]

# a3
ka3 = kmeans(pos_a3_ml[which(pos_a3_ml$Ch == "starter"), "ML"], 1, 25)
pos_a3_ml$ML <- pos_a3_ml$ML-ka3$centers[1, 1]

# calculate mean density(normalized)
pa1_ml <- geom_line(aes(x = ML, after_stat(count/length(pos_a1_ml[,1])), color = Ch), data = pos_a1_ml, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
pa2_ml <- geom_line(aes(x = ML, after_stat(count/length(pos_a2_ml[,1])), color = Ch), data = pos_a2_ml, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
pa3_ml <- geom_line(aes(x = ML, after_stat(count/length(pos_a3_ml[,1])), color = Ch), data = pos_a3_ml, stat = "density", linetype = "dashed", lwd = 0.6, alpha = 0.6, bw = 0.1)
da1_ml <- ggplot_build(ggplot()+pa1_ml+xlim(c(-1, 0.75)))$data[[1]]
da2_ml <- ggplot_build(ggplot()+pa2_ml+xlim(c(-1, 0.75)))$data[[1]]
da3_ml <- ggplot_build(ggplot()+pa3_ml+xlim(c(-1, 0.75)))$data[[1]]
ave_ml <- data.frame(x = da1_ml$x, y = (da1_ml$y+da2_ml$y+da3_ml$y)/3, Ch = rep(c("starter", "vgat", "vglut2"), each = length(da1_ml[, 1])/3)) #rep(x, times, length.out, each)

#plot
ggplot()+
  pa1_ml+
  pa2_ml+
  pa3_ml+
  geom_line(data = ave_ml, aes(x = x, y = y, color = Ch), lwd = 0.8)+
  theme_classic() +
  #scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  #scale_color_manual(values = c("#E3D25A", "#1E00DC", "#B80024"))+
  #scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  xlim(c(-1, 0.75))+
  ylim(c(0, 1.4))+
  labs(y = "Density(normalized)", x = "ML(- kmeans of starters)")
ggsave("M-L density plot.pdf", width = 12, height = 7, units = "cm")
#ggsave("M-L density plot 2.pdf", width = 12, height = 7, units = "cm")

# ######## plot histogram and fitted normal curve
# pos_ml <- rbind(pos_a1_ml, pos_a2_ml, pos_a3_ml)
# bw = 0.11
# pos_ml_fit <- pos_ml %>% # %>%: pipe, like convey x to f(x)
#   group_by(Ch, mice) %>%
#   summarise(mean = mean(ML), sd = sd(ML))
# write.csv(pos_ml_fit, "M-L Gaussian fit.csv")
# pos_ml %>%
#   group_by(Ch, mice) %>%
#   nest(data = c(ML, AP, DV, region)) %>%
#   mutate(y = map(data, ~ dnorm(
#     .$ML, mean = mean(.$ML), sd = sd(.$ML)
#     )*bw*sum(!is.na(.$ML)))) %>% # to rescale the normal curve to the histogram
#   unnest(c(data, y)) %>%
#   
#   ggplot(aes(x = ML, color = Ch, fill = Ch))+
#   geom_histogram(data = pos_ml, lwd = 0.6, binwidth = bw, alpha = 0.5) +
#   geom_line(aes(y = y), color = "black", lwd = 0.6) +
#   theme_classic() +
#   scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   facet_grid(rows = vars(Ch), cols = vars(mice)) +
#   #xlim(c(-1, 0.75))+
#   #ylim(c(0, 0.76))+
#   labs(y = "Counts", x = "ML(- kmeans of starters)")
# ggsave("M-L Gaussian fit.png", width = 20, height = 15, units = "cm")
# 
# ####### E/I of M-L ######
# #E/I
# n = length(da1_ml$x)/3
# da1_ml_ei <- data.frame(x = da1_ml$x[1:n], y = da1_ml$y[(2*n+1):(3*n)]/da1_ml$y[(n+1):(2*n)])
# da2_ml_ei <- data.frame(x = da1_ml$x[1:n], y = da2_ml$y[(2*n+1):(3*n)]/da2_ml$y[(n+1):(2*n)])
# da3_ml_ei <- data.frame(x = da1_ml$x[1:n], y = da3_ml$y[(2*n+1):(3*n)]/da3_ml$y[(n+1):(2*n)])
# ave_ml_ei <- data.frame(x = da1_ml$x[1:n], y = (da1_ml_ei$y+da2_ml_ei$y+da3_ml_ei$y)/3)
# #plot
# ggplot()+
#   geom_line(data = da1_ml_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da2_ml_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = da3_ml_ei, aes(x = x, y = y), lwd = 0.6, linetype = "dashed", alpha = 0.6)+
#   geom_line(data = ave_ml_ei, aes(x = x, y = y), lwd = 0.8)+
#   theme_classic()+
#   scale_color_manual(values = "#383A3F")+
#   theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
#   labs(y = "E/I ratio", x = "ML")+
#   ylim(c(0, 1.19))
# ggsave("M-L E-I.pdf", width = 12, height = 5, units = "cm")
# write.csv(ave_ei, "M-L E-I.csv")


#########################################################################################
###### vgat+ proportion ######
chs <- data.frame(animal = rep(c("a1", "a2", "a3"), times = 2), Mice = rep(c("vgat-cre", "vglut2-cre"), each = 3), perc = 0)
chs_a1 <- as.data.frame(table(pos_a1$Ch))
chs_a2 <- as.data.frame(table(pos_a2$Ch))
chs_a3 <- as.data.frame(table(pos_a3$Ch))
# vgat
chs[1, 3] <- chs_a1[2, 2]/sum(chs_a1[2:3, 2])
chs[2, 3] <- chs_a2[2, 2]/sum(chs_a2[2:3, 2])
chs[3, 3] <- chs_a3[2, 2]/sum(chs_a3[2:3, 2])
# vglut2
chs[4, 3] <- chs_a1[2, 2]/sum(chs_a1[2:3, 2])
chs[5, 3] <- chs_a2[2, 2]/sum(chs_a2[2:3, 2])
chs[6, 3] <- chs_a3[2, 2]/sum(chs_a3[2:3, 2])
write.csv(chs, "vgat proportion.csv")


# plot
ggbarplot(chs, x = "Mice", y = "perc", add = "mean_se",
          color = c("#30A9DE", "#E53A40"), fill = c("#30A9DE", "#E53A40"), 
          position = position_dodge(1), width = 0.5, size = 0.5, 
          ylab = "vgat+ % (non-starters)", ggtheme = theme_classic())+
  stat_compare_means(aes(group = Mice), label = "p.signif", label.x = 1.5)+
  rotate_x_text(angle = 30)+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("identification.pdf", width = 5, height = 7.5, units = "cm")

### mean & se
se <- function(x) sd(x)/sqrt(length(x))
m_s <- data.frame(mice = c("vgat-cre", "vglut2-cre"), mean_perc = 0, se = 0)
m_s[1, 2] <- mean(chs[which(chs$Mice == "vgat-cre"), "perc"])
m_s[1, 3] <- se(chs[which(chs$Mice == "vgat-cre"), "perc"])
m_s[2, 2] <- mean(chs[which(chs$Mice == "vglut2-cre"), "perc"])
m_s[2, 3] <- se(chs[which(chs$Mice == "vglut2-cre"), "perc"])
write.csv(m_s, "mean and sem.csv")


##########################################################################################
###### projection strength ######
proj <- read.csv("count.csv")
proj$region <- factor(proj$region, levels = c("SCs", "contra-retina", "ipsi-retina", "cSCs"))
ggbarplot(proj, x = "region", y = "projection", add = "mean_se",
          color = "mice", fill = "mice", palette = c("#30A9DE", "#E53A40"), 
          position = position_dodge(0.53), width = 0.5, size = 0.5, 
          ylab = "RV+/starters", xlab = "Region(part)", ggtheme = theme_classic())+
  stat_compare_means(aes(group = mice), label = "p.signif", label.x = 1.5, label.y = 14)+
  rotate_x_text(angle = 30)+
  #scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("projection new.pdf", width = 13, height = 8, units = "cm")




###########################################################################################
###### contour density plot of ML&AP ######
ggplot(pos_a1, aes(x = ML, y = AP))+ #plot vglut2 A1
  #stat_density_2d(aes(fill = after_stat(level)), geom = "polygon", contour_var = "count", h = 0.6)+
  geom_density2d_filled(contour_var = "count", h = 0.4)+
  xlim(c(0, 1.8))+
  ylim(c(-5, -3))+
  theme_classic() +
  #scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  scale_fill_manual(values = c("#eeeff6", "#3a196b", "#4F86C6", "#61a8da", "#00d2f1", "#70e1ad", "#54ea65", "#b7ea54", "#eae554", "#e7b233", "#e25523"))+
  facet_grid(rows = vars(Ch))+
  #scale_fill_distiller(palette = "Reds", direction = 1)+
  theme(axis.title = element_text(size = 20), axis.text = element_text(size = 18), legend.text = element_text(size = 16))
ggsave("contour colors2.pdf", width = 17.5, height = 36, units = "cm")

ggplot(pos_a1, aes(x = AP))+
  geom_density(aes(x = AP, after_stat(count), color = Ch), lwd = 0.8, bw = 0.11)+
  theme_classic()+
  scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  #scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  facet_grid(rows = vars(Ch))+
  xlim(c(-5, -3))+
  coord_flip()+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))
ggsave("contour AP density.pdf", width = 10, height = 36, units = "cm")

ggplot(pos_a1, aes(x = ML))+
  geom_density(aes(x = ML, after_stat(count), color = Ch), lwd = 0.8, bw = 0.1)+
  theme_classic()+
  scale_color_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  #scale_fill_manual(values = c("#FFBC42", "#30A9DE", "#E53A40"))+
  #facet_grid(rows = vars(Ch))+
  xlim(c(0, 1.8))+
  #coord_flip()+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))
ggsave("contour ML density.pdf", width = 14.8, height = 6, units = "cm")



###########################################################################################
#### supplementary ####
co <- read.csv("co-staining count.csv")
ggplot(co, aes(x= "", y = perc, fill = type))+
  geom_bar(width = 1, stat = "identity")+
  theme_classic() +
  #scale_color_manual(values = c("#E0E3DA", "#30A9DE", "#E53A40"))+ ##E0E3DA
  scale_fill_manual(values = c("#E0E3DA", "#30A9DE", "#E53A40"))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  labs(y = "Proportion", x = "")+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))
ggsave("co-staining.pdf", width = 10, height = 7, units = "cm")


###########################################################################################
count(vg2_a1[which(vg2_a1$Ch == "starter"), ], vars = "region")
count(vg2_a2[which(vg2_a2$Ch == "starter"), ], vars = "acronym")
count(vg2_a3[which(vg2_a3$Ch == "starter"), ], vars = "acronym")
count(vgat_a1[which(vgat_a1$Ch == "starter"), ], vars = "Region")
count(vgat_a2[which(vgat_a2$Ch == "starter"), ], vars = "acronym")
count(vgat_a3[which(vgat_a3$Ch == "starter"), ], vars = "acronym")

starter_vg2 <- read.csv("starter vg2.csv")
ggplot(starter_vg2, aes(x= mice, y = perc, fill = region))+
  geom_bar(width = 0.5, stat = "identity")+
  theme_classic() +
  #scale_color_manual(values = c("#E0E3DA", "#30A9DE", "#E53A40"))+ ##E0E3DA
  scale_fill_manual(values = c("#D7FFF1", "#8CD790", "#77AF9C", "#285943"))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  labs(y = "Proportion", x = "vglut2-cre")+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))
ggsave("starter vg2.pdf", width = 13, height = 7, units = "cm")

starter_vgat <- read.csv("starter vgat.csv")
ggplot(starter_vgat, aes(x= mice, y = perc, fill = region))+
  geom_bar(width = 0.5, stat = "identity")+
  theme_classic() +
  #scale_color_manual(values = c("#E0E3DA", "#30A9DE", "#E53A40"))+ ##E0E3DA
  scale_fill_manual(values = c("#D7FFF1", "#8CD790", "#77AF9C", "#285943"))+
  theme(axis.title = element_text(size = 15), axis.text = element_text(size = 13))+
  labs(y = "Proportion", x = "vgat-cre")+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))
ggsave("starter vgat.pdf", width = 13, height = 7, units = "cm")




###### data storage ######
### vglut2 ###
vg2_a1 <- pos_a1
vg2_a2 <- pos_a2
vg2_a3 <- pos_a3
### restore ###
pos_a1 <- vg2_a1
pos_a2 <- vg2_a2
pos_a3 <- vg2_a3

### vgat ###
vgat_a1 <- pos_a1
vgat_a2 <- pos_a2
vgat_a3 <- pos_a3
### restore ###
pos_a1 <- vgat_a1
pos_a2 <- vgat_a2
pos_a3 <- vgat_a3



####### additional comparison
#test normality: shapiro.test(), H0 is normal, so p>0.05 then pass the test. suitable for n<5000
### fig 2E
chs = read.csv("vgat proportion.csv")[, -1]
t.test(chs[1:3, 3], 1-chs[1:3, 3], paired = TRUE)
#t.test(chs[1:3, 3], 1-chs[1:3, 3])
t.test(chs[4:6, 3], 1-chs[4:6, 3], paired = T)
t.test(chs[1:3, 3], chs[4:6, 3])


### fig 2D
proj = read.csv("count.csv")[1:18, ]
t.test(proj[1:3, 3], proj[10:12, 3])
t.test(proj[4:6, 3], proj[13:15, 3])
t.test(proj[7:9, 3], proj[16:18, 3])
t.test(proj[c(1:3, 10:12), 3], proj[c(4:6, 13:15), 3], paired = T)
t.test(proj[c(1:3, 10:12), 3], proj[c(7:9, 16:18), 3], paired = T)
t.test(proj[c(7:9, 16:18), 3], proj[c(4:6, 13:15), 3], paired = T)


####* starter core region analysis ######
core_vgat = read.csv("counting cores vgat.csv") 
colnames(core_vgat) = c("animal", "all_vgat", "all_gfp", "vgat_gfp_v5", "vgat_v5", "vgat_gfp", "vgat", "gfp")
core_vgat$group = "vgat"

core_vg2 = read.csv("counting cores vglut2.csv") 
colnames(core_vg2) = c("animal", "all_vg2", "all_gfp", "vg2_gfp_v5", "vg2_v5", "vg2_gfp", "vg2", "gfp")
core_vg2$group = "vg2"

core = data.frame(animal = rep(c("a1", "a2", "a3"), times = 2), group = rep(c("vgat", "vglut2"), each = 3), 
                  v5_marker = 0, vgat_gfp_core = 0, vgat_gfp_rest = 0)

# ratio of V5+ in all the vgat+(vgat-cre mice) or vglut2+(vglut2-cre mice) in the core region
core[1, 3] = sum(core_vgat[1, 4:5])/core_vgat[1, 2]
core[2, 3] = sum(core_vgat[2, 4:5])/core_vgat[2, 2]
core[3, 3] = sum(core_vgat[3, 4:5])/core_vgat[3, 2]
core[4, 3] = sum(core_vg2[1, 4:5])/core_vg2[1, 2]
core[5, 3] = sum(core_vg2[2, 4:5])/core_vg2[2, 2]
core[6, 3] = sum(core_vg2[3, 4:5])/core_vg2[3, 2]

# ratio of vgat+ in RV_GFP in the starter core and the rest
gfp_maker = read.csv("counting all single section.csv")[, -1]

core[1, 4] = core_vgat[1, 6]/(core_vgat[1, 3]-core_vgat[1, 4])
core[2, 4] = core_vgat[2, 6]/(core_vgat[2, 3]-core_vgat[2, 4])
core[3, 4] = core_vgat[3, 6]/(core_vgat[3, 3]-core_vgat[3, 4])
core[4, 4] = 1-core_vg2[1, 6]/(core_vg2[1, 3]-core_vg2[1, 4])
core[5, 4] = 1-core_vg2[2, 6]/(core_vg2[2, 3]-core_vg2[2, 4])
core[6, 4] = 1-core_vg2[3, 6]/(core_vg2[3, 3]-core_vg2[3, 4])

core[1, 5] = (gfp_maker[1, 3]-core_vgat[1, 6])/(sum(gfp_maker[1, 3:4])-(core_vgat[1, 3]-core_vgat[1, 4]))
core[2, 5] = (gfp_maker[2, 3]-core_vgat[2, 6])/(sum(gfp_maker[2, 3:4])-(core_vgat[2, 3]-core_vgat[2, 4]))
core[3, 5] = (gfp_maker[3, 3]-core_vgat[3, 6])/(sum(gfp_maker[3, 3:4])-(core_vgat[3, 3]-core_vgat[3, 4]))
core[4, 5] = (gfp_maker[4, 3]-core_vg2[1, 8])/(sum(gfp_maker[4, 3:4])-(core_vg2[1, 3]-core_vg2[1, 4]))
core[5, 5] = (gfp_maker[5, 3]-core_vg2[2, 8])/(sum(gfp_maker[5, 3:4])-(core_vg2[2, 3]-core_vg2[2, 4]))
core[6, 5] = (gfp_maker[6, 3]-core_vg2[3, 8])/(sum(gfp_maker[6, 3:4])-(core_vg2[3, 3]-core_vg2[3, 4]))



#####** plot ########
# ratio of V5+ in vgat+ or vglut2+
ggbarplot(core, x = "group", y = "v5_marker", add = "mean_se",
          color = "group", fill = "group", 
          #color = c("#30A9DE", "#E53A40"), fill = c("#30A9DE", "#E53A40"), 
          palette = c("vgat" = "#30A9DE", "vglut2" = "#E53A40"),
          position = position_dodge(1), width = 0.5, size = 0.5, 
          ylim = c(0, 1),
          ylab = "V5+% in marker+", ggtheme = theme_classic())+
  stat_compare_means(aes(group = group), label = "p.signif", label.x = 1)+
  stat_compare_means(aes(group = group), label = "p.format", label.x = 1, label.y = 0.5)+
  rotate_x_text(angle = 30)+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("ratio_V5_marker.pdf", width = 8, height = 7.5, units = "cm")

### mean & se
se <- function(x) sd(x)/sqrt(length(x))
summary_v5 = core %>%
  group_by(group) %>%
  summarise(
    mean_v5_marker = mean(v5_marker),
    se_v5_marker = se(v5_marker)
  )

write.csv(summary_v5, "V5_marker_mean_se.csv")



# ratio of vgat+ in vgat-cre or vglut2-cre in core region
ggbarplot(core, x = "group", y = "vgat_gfp_core", add = "mean_se",
          color = "group", fill = "group", 
          #color = c("#30A9DE", "#E53A40"), fill = c("#30A9DE", "#E53A40"), 
          palette = c("vgat" = "#30A9DE", "vglut2" = "#E53A40"),
          position = position_dodge(1), width = 0.5, size = 0.5, 
          ylab = "Vgat+% in non-starter RV core", ggtheme = theme_classic())+
  stat_compare_means(aes(group = group), label = "p.signif", label.x = 1.8)+
  stat_compare_means(aes(group = group), label = "p.format", label.x = 1.8, label.y = 0.9)+
  rotate_x_text(angle = 30)+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("ratio_vgat_non_starter_RV_core.pdf", width = 8, height = 7.5, units = "cm")

### mean & se
se <- function(x) sd(x)/sqrt(length(x))
summary_vgat_core = core %>%
  group_by(group) %>%
  summarise(
    mean_vgat_gfp_core = mean(vgat_gfp_core),
    se_vgat_gfp_core = se(vgat_gfp_core)
  )

write.csv(summary_vgat_core, "vgat_ratio_core_mean_se.csv")


# ratio of vgat+ in vgat-cre or vglut2-cre in peripheral region
ggbarplot(core, x = "group", y = "vgat_gfp_rest", add = "mean_se",
          color = "group", fill = "group", 
          #color = c("#30A9DE", "#E53A40"), fill = c("#30A9DE", "#E53A40"), 
          palette = c("vgat" = "#30A9DE", "vglut2" = "#E53A40"),
          position = position_dodge(1), width = 0.5, size = 0.5, 
          ylim = c(0, 1), 
          ylab = "Vgat+% in non-starter RV peri", ggtheme = theme_classic())+
  stat_compare_means(aes(group = group), label = "p.signif", label.x = 1.8, label.y = 1)+
  stat_compare_means(aes(group = group), label = "p.format", label.x = 1.8, label.y = 0.9)+
  rotate_x_text(angle = 30)+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("ratio_vgat_non_starter_RV_peri.pdf", width = 8, height = 7.5, units = "cm")

### mean & se
se <- function(x) sd(x)/sqrt(length(x))
summary_vgat_peri = core %>%
  group_by(group) %>%
  summarise(
    mean_vgat_gfp_rest = mean(vgat_gfp_rest),
    se_vgat_gfp_rest = se(vgat_gfp_rest)
  )

write.csv(summary_vgat_peri, "vgat_ratio_peri_mean_se.csv")

mean(core$vgat_gfp_rest[1:3])
se(core$vgat_gfp_rest[1:3])
mean(core$vgat_gfp_rest[4:6])
se(core$vgat_gfp_rest[4:6])

#write.csv(core, "vgat_ratio_comparison_individuals.csv")

# ratio of vgat+ in vgat-cre or vglut2-cre in peripheral region
data = read.csv("vgat_ratio_comparison_individuals.csv")
ggbarplot(data, x = "group", y = "vgat_gfp", add = "mean_se",
          color = "group", fill = "group", 
          #color = c("#30A9DE", "#E53A40"), fill = c("#30A9DE", "#E53A40"), 
          #palette = c("vgat" = "#30A9DE", "vglut2" = "#E53A40"),
          position = position_dodge(1), width = 0.5, size = 0.5, 
          ylim = c(0, 1), 
          ylab = "Vgat+% in non-starter RV", ggtheme = theme_classic())+
  stat_compare_means(aes(group = group), method = "anova", label.x = 2, label.y = 0.9)+
  #stat_compare_means(aes(group = group), method = "anova", label = "p.format", label.x = 1.8, label.y = 0.9)+
  stat_compare_means(label = "p.signif", method = "t.test", ref.group = ".all.", label.y = 0.98)+ #pairwise comparison with global mean
  rotate_x_text(angle = 30)+
  scale_y_continuous(labels = scales::percent_format(accuracy = 1))+
  theme(axis.title = element_text(size = 13), axis.text = element_text(size = 13))
ggsave("ratio_vgat_non_starter_RV_comparison.pdf", width = 14, height = 8, units = "cm")

### mean & se
se <- function(x) sd(x)/sqrt(length(x))
summary_vgat = data %>%
  group_by(group) %>%
  summarise(
    mean_vgat_gfp = mean(vgat_gfp),
    se_vgat_gfp = se(vgat_gfp)
  )