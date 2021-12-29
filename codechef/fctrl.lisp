(defun z (n)
  (declare (fixnum n))
  (do ((ans 0)
       (i 1 (1+ i)))
      ((> i (floor (log n 5))) ans)
      (declare (fixnum i ans))
      (incf ans (floor n (expt 5 i)))))


(defun main ()
  (dotimes (_ (read))
    (format t "~A~%" (z (read)))))

(main)
