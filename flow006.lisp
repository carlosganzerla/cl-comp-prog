(defun read-integer ()
  (do ((val 0) 
       (c (char-code (read-char)) (char-code (read-char))))
      ((or (> c 57) (< c 48)) val)
      (declare (fixnum c val))
      (incf val (- c 48))))

(defun main ()
  (let ((tests (read)))
    (declare (fixnum tests))
    (mapcar #'print
            (loop for i from 1 to tests collect (read-integer)))))

(main)
