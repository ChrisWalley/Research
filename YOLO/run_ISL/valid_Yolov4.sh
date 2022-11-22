if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISL_data/obj.data cfg/yolov4-isl.cfg backup/yolov4-isl.backup < ISL_data/valid.txt > results/Yolov4-isl_valid_cpu_results.txt
else
    ./darknet detector test ISL_data/obj.data cfg/yolov4-isl.cfg backup/yolov4-isl.backup < ISL_data/valid.txt > results/Yolov4-isl_valid_results.txt
fi
