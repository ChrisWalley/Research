if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov4.cfg backup/yolov4.backup < ASL_data/valid.txt > results/Yolov4_valid_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov4.cfg backup/yolov4.backup < ASL_data/valid.txt > results/Yolov4_valid_results.txt
fi
