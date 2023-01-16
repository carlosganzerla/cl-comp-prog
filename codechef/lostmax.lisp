(defun main ()
  (dotimes (_ (read))
    (let ((lst (read-from-string (format nil "#(~A)" (read-line)))))
      (do ((max1 0)
           (max2 0)
           (i 0 (1+ i)))
          ((>= i (length lst)) (if (= (1- (length lst)) max1)
                                   (print max2)
                                   (print max1)))
          (cond ((> (aref lst i) max1) (setf max2 max1 
                                             max1 (aref lst i)))
                ((> (aref lst i) max2) (setf max2 (aref lst i))))))))


(main)


