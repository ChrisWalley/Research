if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov4.cfg backup/yolov4.backup < ASL_data/test.txt > results/Yolov4_test_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov4.cfg backup/yolov4.backup < ASL_data/test.txt > results/Yolov4_test_results.txt
fi
