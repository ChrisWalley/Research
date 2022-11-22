if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ISL_data/obj.data cfg/yolov4-isl.cfg backup/yolov4-isl.backup < ISL_data/test.txt > results/Yolov4-isl_test_cpu_results.txt
else
    ./darknet detector test ISL_data/obj.data cfg/yolov4-isl.cfg backup/yolov4-isl.backup < ISL_data/test.txt > results/Yolov4-isl_test_results.txt
fi
