(defun read-multiple ()
  (values-list (read-from-string (concatenate 'string "(" (read-line) ")"))))

(defun main ()
  (multiple-value-bind (withdrawal balance) (read-multiple)
    (if (and (= 0 (mod withdrawal 5))
             (>= balance (+ withdrawal 0.5)))
        (format t "~,2F~%"(- balance (+ withdrawal 0.5)))
        (format t "~,2F~%" balance))))

(main)
